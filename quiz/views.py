from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz, Question,Option
from .serializers import QuizSerializer, QuestionSerializer

class QuizListAPIView(APIView):
    def get(self, request):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

class QuizQuestionsAPIView(APIView):
    def get(self, request, quiz_id):
        questions = Question.objects.filter(quiz__id=quiz_id)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
class SubmitQuizView(APIView):
    def post(self, request, quiz_id):
        data = request.data  # expecting {question_id: selected_option_id, ...}
        correct = 0
        total = 0
        results = []

        for question_id, selected_option_id in data.items():
            try:
                question = Question.objects.get(id=question_id, quiz_id=quiz_id)
                selected_option = Option.objects.get(id=selected_option_id, question=question)
                correct_option = Option.objects.filter(question=question, is_correct=True).first()
                is_correct = selected_option.is_correct
                if is_correct:
                    correct += 1
                total += 1
                results.append({
                    "question": question.text,
                    "your_answer": selected_option.text,
                    "correct_answer": correct_option.text,
                    "is_correct": is_correct
                })
            except:
                continue

        return Response({
            "score": correct,
            "total": total,
            "results": results
        }, status=status.HTTP_200_OK)
def quiz_page(request):
    return render(request, 'quiz/quiz.html')
# Create your views here.
