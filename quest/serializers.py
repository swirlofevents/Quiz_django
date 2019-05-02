from rest_framework import serializers
from quest.models import Questions, AnswersModel, ResultAnswers


#class AnswersSerializer(serializers.ModelSerializer)

class AnswersModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = AnswersModel
        fields = ("answer",)


class QuestionSerializers(serializers.ModelSerializer):


    answers = AnswersModelSerializers(many=True)
    class Meta:
        model = Questions
        fields = ("id", "question", "answers")


class ResultAnswersSerializers(serializers.ModelSerializer):

    class Meta:
        model = ResultAnswers
        fields = ("answers",)
