from django.contrib import admin
from .models import Subject, Assignment, Question, Answer 

myModels = [Subject, Assignment, Question, Answer]
admin.site.register(myModels)
