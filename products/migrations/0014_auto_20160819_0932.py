# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-19 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20160819_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_b2b',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Χονδρικής'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_internet',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Internet'),
        ),
    ]
