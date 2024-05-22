from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Question(models.Model):
    image = models.ImageField(upload_to='questions/', verbose_name='Изображение')
    text = models.CharField(max_length=255, verbose_name='Текст вопроса')
    option_a = models.CharField(max_length=255, verbose_name='Вариант A')
    option_b = models.CharField(max_length=255, verbose_name='Вариант Б')
    option_c = models.CharField(max_length=255, verbose_name='Вариант В')
    option_d = models.CharField(max_length=255, verbose_name='Вариант Г')
    correct_answer = models.CharField(max_length=1, choices=[('A', 'А'), ('B', 'Б'), ('C', 'В'), ('D', 'Г')],
                                      verbose_name='Правильный ответ')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Ticket(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    questions = models.ManyToManyField(Question, verbose_name='Вопросы')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return self.name


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    answer = models.CharField(max_length=255, verbose_name='Ответ')
    is_correct = models.BooleanField(verbose_name='Правильный')

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'

    def __str__(self):
        return f'{self.user} - {self.question}'
