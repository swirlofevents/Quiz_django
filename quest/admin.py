from django.contrib import admin
from quest.models import Questions, AnswersModel, ResultAnswers


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "ans_the_quest")

    def ans_the_quest(self, obj):
        return "\n".join([answersmodel.answer for answersmodel in obj.answers.all()])

class AnswersModelAdmin(admin.ModelAdmin):

    list_display = ("id", "answer")

class ResultAnswersAdmin(admin.ModelAdmin):

    list_display = ("id", "answers")

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(ResultAnswers, ResultAnswersAdmin)
admin.site.register(AnswersModel, AnswersModelAdmin)
