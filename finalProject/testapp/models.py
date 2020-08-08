from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class UserDetail(models.Model):
    Full_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    current_address = models.CharField(max_length=100)