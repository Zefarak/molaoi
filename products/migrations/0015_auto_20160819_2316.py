# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-19 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20160819_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Κωδικός Τιμολογίου'),
        ),
    ]