# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-12 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee_django_exam', '0002_auto_20180112_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=180, verbose_name='\u987b\u77e5\u6807\u9898'),
        ),
    ]
