from django.contrib import admin
from .models import AssignmentPDF, AssignmentGrades, AssignmentSubmit

# Register your models here.
admin.site.register(AssignmentPDF)
admin.site.register(AssignmentSubmit)
admin.site.register(AssignmentGrades)
