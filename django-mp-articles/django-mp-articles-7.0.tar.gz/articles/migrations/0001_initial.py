# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-10 12:10
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=b'article_logos')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(max_length=50000, verbose_name='Text')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Created')),
                ('author', models.CharField(blank=True, max_length=255, verbose_name='Author')),
                ('is_comments_enabled', models.BooleanField(default=True, verbose_name='Is comments enabled')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, unique=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Article tag',
                'verbose_name_plural': 'Article tags',
            },
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('slug', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Article type',
                'verbose_name_plural': 'Article types',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='articles.ArticleTag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.ArticleType', verbose_name='Type'),
        ),
    ]
