# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-07 05:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoS', '0022_auto_20160805_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyincomegreg',
            name='title',
            field=models.CharField(default='2016-08-07', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='lianiki_order',
            name='day_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 7, 8, 34, 54, 873141)),
        ),
        migrations.AlterField(
            model_name='lianiki_order',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 8, 7, 8, 34, 54, 873141), max_length=50),
        ),
    ]