# Generated by Django 3.0.3 on 2020-08-25 15:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studymaterial', '0004_auto_20200812_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='classuser',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
