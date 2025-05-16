from django.urls import path
from .views import QuizListAPIView, QuizQuestionsAPIView,SubmitQuizView,quiz_page
urlpatterns = [
    path('quizzes/', QuizListAPIView.as_view()),
    path('quizzes/<int:quiz_id>/questions/', QuizQuestionsAPIView.as_view()),
    path('quizzes/<int:quiz_id>/submit/', SubmitQuizView.as_view(), name='submit-quiz'),
    path('', quiz_page, name='quiz-page'),
]
