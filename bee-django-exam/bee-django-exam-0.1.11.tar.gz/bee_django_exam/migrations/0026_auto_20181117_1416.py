# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-17 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee_django_exam', '0025_userstartexam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexamrecord',
            name='status',
            field=models.IntegerField(blank=True, choices=[(-1, '\u672a\u62a5\u540d'), (-2, '\u5df2\u62a5\u540d'), (1, '\u901a\u8fc7'), (2, '\u672a\u901a\u8fc7'), (3, '\u5173\u95ed')], default=-1, null=True, verbose_name='\u72b6\u6001'),
        ),
    ]
