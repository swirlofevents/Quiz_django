from rest_framework.response import Response
from rest_framework.views import APIView
from quest.models import Questions, AnswersModel
from rest_framework import permissions
from quest.serializers import QuestionSerializers, AnswersModelSerializers, ResultAnswersSerializers


class Question(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self ,request):

        questions = Questions.objects.all()
        serializer_quest = QuestionSerializers(questions, many=True)
        return Response(serializer_quest.data)

class Results(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        ans = ResultAnswers.objects(answers=request.data)
        ans.add()
