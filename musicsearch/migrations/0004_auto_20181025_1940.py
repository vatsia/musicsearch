# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-25 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musicsearch', '0003_auto_20181025_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasearch',
            name='search_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
