from django.db import models
from users.models import User


class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct Answer', default=False)

    def __str__(self):
        return self.text 