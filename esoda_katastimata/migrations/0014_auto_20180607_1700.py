# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-07 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esoda_katastimata', '0013_auto_20180406_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthesoda',
            name='title',
            field=models.CharField(default='June', max_length=64),
        ),
    ]
