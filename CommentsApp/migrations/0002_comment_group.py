# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GroupsApp', '0005_auto_20161208_0611'),
        ('CommentsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GroupsApp.Group'),
        ),
    ]