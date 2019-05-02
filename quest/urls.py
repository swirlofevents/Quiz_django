from django.urls import path
from quest.views import *


urlpatterns = [
    path('question/', Question.as_view()),

    path('results/', Results.as_view()),

    # path('answer/', Answers.as_view())
    ]
