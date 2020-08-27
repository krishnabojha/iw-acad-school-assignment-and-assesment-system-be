# Generated by Django 3.1 on 2020-08-27 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studymaterial', '0004_auto_20200812_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_title', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('classid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studymaterial.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='studymaterial.choice')),
                ('assignment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='studymaterial.assignment')),
                ('choices', models.ManyToManyField(blank=True, to='studymaterial.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentPDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_title', models.CharField(blank=True, max_length=150, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='files/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('classid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studymaterial.classroom')),
            ],
        ),
    ]
