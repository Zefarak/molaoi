# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-23 19:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoS', '0050_auto_20160823_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lianiki_order',
            name='day_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 23, 22, 26, 25, 534020)),
        ),
        migrations.AlterField(
            model_name='lianiki_order',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 8, 23, 22, 26, 25, 534020), max_length=50),
        ),
    ]
