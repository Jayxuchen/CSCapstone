# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(default=0, upload_to=b'static/projectimages'),
        ),
    ]
