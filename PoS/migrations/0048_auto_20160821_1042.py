# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-21 07:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoS', '0047_auto_20160821_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lianiki_order',
            name='day_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 21, 10, 42, 33, 105084)),
        ),
        migrations.AlterField(
            model_name='lianiki_order',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 8, 21, 10, 42, 33, 105084), max_length=50),
        ),
    ]