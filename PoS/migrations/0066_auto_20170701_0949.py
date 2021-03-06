# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-01 06:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoS', '0065_auto_20170609_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyincomegreg',
            name='title',
            field=models.CharField(default='2017-07-01', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='lianiki_order',
            name='day_added',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 1, 9, 49, 49, 934101)),
        ),
        migrations.AlterField(
            model_name='lianiki_order',
            name='title',
            field=models.CharField(default=datetime.datetime(2017, 7, 1, 9, 49, 49, 934101), max_length=50),
        ),
        migrations.AlterField(
            model_name='monthlyincomegreg',
            name='title',
            field=models.CharField(default='July', max_length=64),
        ),
    ]
