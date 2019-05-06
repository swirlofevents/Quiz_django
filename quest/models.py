from django.db import models


class AnswersModel(models.Model):

    answer = models.TextField(max_length=400, verbose_name="Ответ")
    votes = models.CharField(max_length=4096, verbose_name="кол-во голосов")

#    def __str__(self):
#        return str(self.answer)

class Questions(models.Model):

    question = models.TextField(max_length=400, verbose_name="Вопрос")
    answers = models.ManyToManyField(AnswersModel, verbose_name="Ответ", related_name="ans_the_quest")

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return str(self.answers)


class ResultAnswers(models.Model):

    answers = models.TextField(verbose_name="Ответы на вопросы")
