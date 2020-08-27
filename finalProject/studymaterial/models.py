from django.db import models


class ClassRoom(models.Model):
    classname = models.CharField(max_length = 100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.classname


class StudyMaterial(models.Model):
    file_title = models.CharField(max_length=150,blank = True, null = True)
    video_title = models.CharField(max_length=150,blank = True, null = True)
    files = models.FileField(upload_to = 'files/', blank = True, null = True)
    videos = models.FileField(upload_to = 'videos/', blank = True, null = True)
    classid = models.ForeignKey(ClassRoom, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class AssignmentPDF(models.Model):
    file_title = models.CharField(max_length=150, blank=True, null=True)
    files = models.FileField(upload_to='files/', blank=True, null=True)
    classid = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_title


class Assignment(models.Model):
    file_title = models.CharField(max_length=150, blank=True, null=True)
    classid = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_title


class Choice(models.Model):
    file_title = models.CharField(max_length=50)

    def __str__(self):
        return self.file_title


class Question(models.Model):
    question = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice, blank=True)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    order = models.SmallIntegerField()

    def __str__(self):
        return self.question

