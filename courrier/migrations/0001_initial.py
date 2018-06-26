# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-17 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_order', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('shipping_cost', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('paid_value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('is_paid', models.BooleanField(default=True)),
                ('is_cancel', models.BooleanField(default=False)),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courrier.PaymentMethod')),
                ('shipping_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courrier.Shipping')),
            ],
        ),
    ]