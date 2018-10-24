# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-24 12:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicsearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=126),
        ),
        migrations.AlterField(
            model_name='datasearch',
            name='search_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 24, 12, 6, 32, 213813)),
        ),
    ]