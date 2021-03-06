# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-26 08:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transcations', '0002_auto_20160526_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='paypersonbasicsalarycost',
            name='day_added',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 5, 26, 8, 1, 32, 136992, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypersonbasicsalarycost',
            name='day_expire',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Πληρωμή μέχρι .....'),
        ),
        migrations.AddField(
            model_name='paypersonbasicsalarycost',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Αξία'),
        ),
        migrations.AlterField(
            model_name='paypersonbasicsalarycost',
            name='title',
            field=models.CharField(max_length=64, unique=True, verbose_name='Περιγραφή'),
        ),
    ]
