# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompaniesApp', '0004_auto_20161208_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
        migrations.AlterField(
            model_name='engineer',
            name='projects',
            field=models.ManyToManyField(to='ProjectsApp.Project'),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]