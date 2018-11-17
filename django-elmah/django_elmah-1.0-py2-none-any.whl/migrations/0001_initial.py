# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-11 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjelmahHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=150)),
                ('api_key', models.CharField(max_length=128)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DjelmahLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=128)),
                ('path', models.CharField(max_length=2048)),
                ('username', models.CharField(max_length=32)),
                ('datetime', models.DateTimeField()),
                ('error_type', models.CharField(max_length=64)),
                ('error_message', models.TextField(blank=True)),
                ('status_code', models.CharField(blank=True, max_length=8)),
                ('raw_html', models.TextField(blank=True)),
            ],
        ),
    ]
