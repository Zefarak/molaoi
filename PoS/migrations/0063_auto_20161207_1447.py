# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-07 12:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoS', '0062_auto_20161207_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lianiki_order',
            name='day_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 14, 47, 29, 63081)),
        ),
        migrations.AlterField(
            model_name='lianiki_order',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 12, 7, 14, 47, 29, 63081), max_length=50),
        ),
    ]