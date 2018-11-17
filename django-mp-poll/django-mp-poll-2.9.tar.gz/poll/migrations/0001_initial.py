# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-14 10:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Poll',
                'verbose_name_plural': 'Polls',
            },
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('votes', models.IntegerField(default=0, editable=False)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll')),
            ],
            options={
                'ordering': ['value'],
                'verbose_name': 'Poll choice',
                'verbose_name_plural': 'Poll choices',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('ip', models.CharField(db_index=True, editable=False, max_length=40)),
                ('session', models.CharField(db_index=True, editable=False, max_length=40)),
                ('user_agent', models.CharField(editable=False, max_length=255)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.PollChoice')),
                ('poll', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='poll.Poll')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Vote',
                'verbose_name_plural': 'Votes',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pollchoice',
            unique_together=set([('poll', 'value')]),
        ),
    ]
