# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 15:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0002_project_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='photo',
        ),
    ]
