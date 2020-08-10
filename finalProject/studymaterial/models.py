from django.db import models

class ClassRoom(models.Model):
    classname = models.CharField(max_length = 100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.classname

class StudyMaterial(models.Model):
    files = models.FileField(upload_to = 'static/files', blank = True, null = True)
    videos = models.FileField(upload_to = 'static/videos', blank = True, null = True)
    classid = models.ForeignKey(ClassRoom, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
