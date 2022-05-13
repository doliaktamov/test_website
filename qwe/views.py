from re import T
from tkinter import S
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from qwe import permissions
from .serializers import *
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import Question, Answer, Result
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

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = False
        serializer.save()
    
class QuestionAPIViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAdminAuthentiocation]

class UserCreateAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.validated_data['is_valid'] = True
        serializer.save()

class ResultCreateAPIView(ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    