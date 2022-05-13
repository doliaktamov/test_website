from dataclasses import field
from urllib import request
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Answer, Question, Result, Category
from datetime import datetime

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            is_staff = validated_data['is_staff']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
    
    def validate(self, data):
        if data['question']:
            question = data['question']
            if question.type == 'Выбор':
                raise serializers.ValidationError('У данного вопроса тип "Выбор"')
        return data
    
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['question', 'answer', ]
        read_only_fields = ['user',]

    def validate(self, data):
        if data['question']:
            question = data['question']
            answer = data['answer']
            if question.type == 'выбор':
                raise serializers.ValidationError('У данного вопроса тип "выбор". Ответ не из выбора')
        return data

    def validate_time(self, data):
        if request.method == 'POST':
            time = data['time']
            question = data['question']
            if (datetime.now() - time).minutes > question.category.time_limit:
                raise serializers.ValidationError('Time is up')
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'