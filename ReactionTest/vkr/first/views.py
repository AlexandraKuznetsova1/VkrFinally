from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, UserAnswer, Ticket
import random


def home(request):
    return render(request, 'first/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Привет, {username}, ваш аккаунт был успешно создан')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'first/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'first/profile.html')


@login_required()
def take_test(request):
    tickets = Ticket.objects.all()
    selected_ticket = random.choice(tickets)
    questions = selected_ticket.questions.all()
    return render(request, 'first/test.html', {'questions': questions, 'ticket': selected_ticket})


@login_required
def submit_test(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return redirect('home')

        questions = ticket.questions.all()

        correct_answers = 0
        total_questions = questions.count()

        for question in questions:
            question_id = str(question.id)
            user_answer = request.POST.get(f'question_{question_id}')
            answered = request.POST.get(f'answered_{question_id}') == "true"
            is_correct = (user_answer == question.correct_answer) if answered else False

            if is_correct:
                correct_answers += 1

            UserAnswer.objects.create(
                user=request.user,
                question=question,
                answer=user_answer if answered else "No Answer",
                is_correct=is_correct
            )

        # Сохраняем результаты в сессии
        request.session['correct_answers'] = correct_answers
        request.session['total_questions'] = total_questions

        return redirect('result_page')

    return redirect('home')


@login_required
def result_page(request):
    correct_answers = request.session.get('correct_answers', 0)
    total_questions = request.session.get('total_questions', 0)
    return render(request, 'first/result.html', {
        'correct_answers': correct_answers,
        'total_questions': total_questions
    })
