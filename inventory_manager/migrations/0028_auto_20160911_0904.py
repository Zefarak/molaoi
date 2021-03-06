# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-11 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0027_auto_20160904_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payorders',
            name='payment_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory_manager.PaymentMethod', verbose_name='Τρόπος Πληρωμής'),
        ),
        migrations.AlterField(
            model_name='payorders',
            name='value_portion',
            field=models.CharField(choices=[('a', 'Εξόφληση συνολικής αξιας'), ('b', 'Δόσεις')], default='b', max_length=1),
        ),
        migrations.AlterField(
            model_name='vendordepositorderpay',
            name='day_added',
            field=models.DateField(verbose_name='Ημερομηνία Πληρωμής'),
        ),
        migrations.AlterField(
            model_name='vendordepositorderpay',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_manager.PaymentMethod', verbose_name='Τρόπος Πληρωμής'),
        ),
        migrations.AlterField(
            model_name='vendordepositorderpay',
            name='value',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Ποσό πληρωμής'),
        ),
    ]
