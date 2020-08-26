# Generated by Django 3.0.3 on 2020-08-26 06:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studymaterial', '0005_classroom_classuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='classuser',
            field=models.ManyToManyField(related_name='classuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
