# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-12 09:45
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='\u8003\u7ea7\u540d\u79f0')),
                ('order_by', models.IntegerField(blank=True, default=0, verbose_name='\u987a\u5e8f')),
                ('is_show', models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a')),
                ('cert_image', models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location=b'media/exam_cert'), upload_to=b'')),
            ],
            options={
                'ordering': ['order_by'],
                'db_table': 'bee_django_exam_grade',
            },
        ),
        migrations.CreateModel(
            name='UserExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_title', models.CharField(max_length=180, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('is_passed', models.BooleanField(default=False)),
                ('result', models.CharField(blank=True, max_length=180, null=True, verbose_name='\u6210\u7ee9')),
                ('info', models.TextField(blank=True, null=True, verbose_name='\u5176\u4ed6')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bee_django_exam_grade', to='bee_django_exam.Grade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bee_django_exam_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'bee_django_exam_user_exam',
            },
        ),
    ]
