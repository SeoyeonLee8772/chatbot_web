from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class UserInformation(models.Model):
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    birth = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    univname = models.CharField(max_length=20)

class University(models.Model):
    univname = models.CharField(max_length=20)
    major = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)

class Chatbot(models.Model):
    data_id = models.CharField(max_length=20)
    questionData = models.CharField(max_length=40)
    answerData = models.CharField(max_length=40)

class ChatbotUI(models.Model):
    user_id = models.CharField(max_length=30)
    data_id = models.CharField(max_length=20)
    userQuestion = models.CharField(max_length=40)