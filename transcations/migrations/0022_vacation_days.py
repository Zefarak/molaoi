# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-14 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcations', '0021_auto_20180607_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation',
            name='days',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
