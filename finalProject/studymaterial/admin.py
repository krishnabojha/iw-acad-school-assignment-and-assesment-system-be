from django.contrib import admin
from .models import ClassRoom, StudyMaterial, Assignment, AssignmentPDF, Choice, Question

admin.site.register(ClassRoom)
admin.site.register(StudyMaterial)
admin.site.register(AssignmentPDF)
admin.site.register(Assignment)
admin.site.register(Choice)
admin.site.register(Question)
