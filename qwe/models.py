from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Question(models.Model):
    text = models.CharField(max_length=255)
    TYPE_CHOICES = (
        ('Текст', 'Text'),
        ('выбор', 'one option')
    )
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)

    def __str__(self):
        return self.text
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    
class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    time = models.IntegerField()

    def __str__(self):
        return self.user.username