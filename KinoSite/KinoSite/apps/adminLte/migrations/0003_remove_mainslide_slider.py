# Generated by Django 3.1.5 on 2021-01-27 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminLte', '0002_auto_20210127_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainslide',
            name='slider',
        ),
    ]
