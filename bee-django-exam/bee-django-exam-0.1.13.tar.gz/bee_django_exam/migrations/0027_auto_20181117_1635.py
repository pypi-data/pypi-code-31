# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-17 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee_django_exam', '0026_auto_20181117_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='is_require',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u5fc5\u9009'),
        ),
    ]
