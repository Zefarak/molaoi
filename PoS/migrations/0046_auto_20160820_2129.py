# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-20 18:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoS', '0045_auto_20160819_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyincomegreg',
            name='title',
            field=models.CharField(default='2016-08-20', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='lianiki_order',
            name='day_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 20, 21, 29, 54, 772442)),
        ),
        migrations.AlterField(
            model_name='lianiki_order',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 8, 20, 21, 29, 54, 772442), max_length=50),
        ),
    ]
