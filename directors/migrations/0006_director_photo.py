# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directors', '0005_auto_20170922_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='photo',
            field=models.ImageField(default='none.png', upload_to=''),
        ),
    ]
