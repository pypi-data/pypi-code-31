# Generated by Django 2.1.1 on 2018-10-01 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("open_widget_framework", "0001_initial")]

    operations = [
        migrations.RenameField(
            model_name="widgetinstance", old_name="widget_type", new_name="widget_class"
        )
    ]
