# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 20:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmenus', '0021_auto_20170106_2352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flatmenuitem',
            options={'ordering': ('sort_order',), 'verbose_name': 'menu item', 'verbose_name_plural': 'menu items'},
        ),
        migrations.AlterModelOptions(
            name='mainmenuitem',
            options={'ordering': ('sort_order',), 'verbose_name': 'menu item', 'verbose_name_plural': 'menu items'},
        ),
    ]
