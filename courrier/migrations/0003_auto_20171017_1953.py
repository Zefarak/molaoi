# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-17 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courrier', '0002_auto_20171017_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weborder',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weborder',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]