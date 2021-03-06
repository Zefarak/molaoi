# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-27 05:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transcations', '0003_auto_20160526_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayPersonDailyCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Περιγραφή')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Αξία')),
                ('day_added', models.DateField(auto_now=True)),
                ('day_expire', models.DateField(default=django.utils.timezone.now, verbose_name='Πληρωμή μέχρι .....')),
            ],
        ),
        migrations.CreateModel(
            name='PayPersonHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Περιγραφή')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Αξία')),
                ('day_added', models.DateField(auto_now=True)),
                ('day_expire', models.DateField(default=django.utils.timezone.now, verbose_name='Πληρωμή μέχρι .....')),
            ],
        ),
        migrations.CreateModel(
            name='PayPersonWeeklyCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Περιγραφή')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Αξία')),
                ('day_added', models.DateField(auto_now=True)),
                ('day_expire', models.DateField(default=django.utils.timezone.now, verbose_name='Πληρωμή μέχρι .....')),
            ],
        ),
    ]
