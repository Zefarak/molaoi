# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-21 17:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoS', '0048_auto_20160821_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lianiki_order',
            name='day_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 21, 20, 53, 42, 322912)),
        ),
        migrations.AlterField(
            model_name='lianiki_order',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 8, 21, 20, 53, 42, 322912), max_length=50),
        ),
    ]
