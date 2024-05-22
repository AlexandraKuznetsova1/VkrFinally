from django.contrib import admin
from .models import Question, UserAnswer, Ticket


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'correct_answer')
    search_fields = ('text',)
    list_filter = ('correct_answer',)
    fields = ('image', 'text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer')
    verbose_name = 'Вопрос'
    verbose_name_plural = 'Вопросы'


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'is_correct')
    search_fields = ('user__username', 'question__text')
    list_filter = ('is_correct',)
    verbose_name = 'Ответ пользователя'
    verbose_name_plural = 'Ответы пользователей'


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('questions',)
    verbose_name = 'Билет'
    verbose_name_plural = 'Билеты'


admin.site.register(Question, QuestionAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)
admin.site.register(Ticket, TicketAdmin)
