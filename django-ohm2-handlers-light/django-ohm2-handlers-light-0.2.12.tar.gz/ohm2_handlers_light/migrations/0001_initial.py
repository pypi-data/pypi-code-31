# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(max_length=2048, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('app', models.CharField(max_length=2048)),
                ('code', models.IntegerField(default=-1)),
                ('message', models.TextField(default='')),
                ('extra', models.TextField(default='')),
                ('ins_filename', models.CharField(blank=True, default='', max_length=2048, null=True)),
                ('ins_lineno', models.IntegerField(blank=True, default=0, null=True)),
                ('ins_function', models.CharField(blank=True, default='', max_length=2048, null=True)),
                ('ins_code_context', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
