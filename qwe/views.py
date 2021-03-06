from unicodedata import category
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from qwe import permissions
from .serializers import *
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import Question, Answer, Result, Category
from rest_framework.viewsets import ModelViewSet

User = get_user_model()

class AdminCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = True
        serializer.save()

    
class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAdminAuthentiocation]

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAdminAuthentiocation, ]

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = False
        serializer.save()

class ResultCreateAPIView(ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser, ]