# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]
