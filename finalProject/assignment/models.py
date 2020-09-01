from django.db import models
from studymaterial.models import ClassRoom
from django.contrib.auth.models import User

class AssignmentPDF(models.Model):
    file_title = models.CharField(max_length=150, blank=True, null=True)
    files = models.FileField(upload_to='files/', blank=True, null=True)
    due_date = models.CharField(max_length=20, blank= True, null= True)
    classid = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_title

class AssignmentSubmit(models.Model):
    assignment_id = models.ForeignKey(AssignmentPDF, on_delete=models.CASCADE )
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    files = models.FileField(upload_to='files/submission', blank=True, null=True)

    def __str__(self):
        return "Assignment of user :"+self.submitter.username + " on assignment title:"+self.assignment_id.file_title

class AssignmentGrades(models.Model):
    submitted_asignment = models.OneToOneField(AssignmentSubmit, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True)

