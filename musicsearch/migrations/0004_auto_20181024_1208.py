# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-24 12:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicsearch', '0003_auto_20181024_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasearch',
            name='search_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 24, 12, 8, 19, 261337)),
        ),
    ]