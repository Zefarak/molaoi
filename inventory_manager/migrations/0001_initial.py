# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-25 05:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40, verbose_name='Αριθμός Παραστατικού')),
                ('date', models.DateField(verbose_name='Ημερομηνία')),
                ('status', models.CharField(choices=[('a', 'Ολοκληρώθηκε'), ('d', 'Δόσεις'), ('p', 'Σε αναμονή'), ('c', 'Ακυρώθηκε')], default='p', max_length=1, verbose_name='Σε εξέλιξη')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='')),
                ('total_price_no_discount', models.DecimalField(decimal_places=3, default=0, max_digits=9, verbose_name='Αξία προ έκπτωσης')),
                ('total_discount', models.DecimalField(decimal_places=3, default=0, max_digits=9, verbose_name='Αξία έκπτωσης')),
                ('total_price_after_discount', models.DecimalField(decimal_places=3, default=0, max_digits=9, verbose_name='Αξία μετά την έκπτωση')),
                ('total_taxes', models.DecimalField(decimal_places=3, default=0, max_digits=9, verbose_name='Φ.Π.Α')),
                ('cost_transfer', models.DecimalField(decimal_places=3, default=0, max_digits=9, verbose_name='Κόστος Μεταφοράς/Επιπλέον Κόστος')),
                ('total_price', models.DecimalField(decimal_places=3, default=0, max_digits=9, verbose_name='Τελική Αξία')),
                ('credit_balance', models.DecimalField(decimal_places=3, default=0, max_digits=9, verbose_name='Πιστωτικό υπόλοιπο')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Supply', verbose_name='Προμηθευτής')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Τιμή Μονάδας')),
                ('discount', models.IntegerField(default=0, max_length=3, verbose_name='Εκπτωση')),
                ('taxes', models.CharField(choices=[('a', '13'), ('b', '23')], default='b', max_length=1, verbose_name='ΦΠΑ')),
                ('qty', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ποσότητα')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_manager.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Προϊόν')),
            ],
            options={
                'ordering': ['product'],
            },
        ),
        migrations.CreateModel(
            name='PayOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Ημερομηνία')),
                ('way_of_pay', models.CharField(choices=[('a', 'Μετρητά'), ('b', 'Πιστωτική'), ('c', 'Μέσω Τραπέζης')], default='a', max_length=1, verbose_name='Τρόπος Εξόφλησης')),
                ('receipt', models.CharField(default='---', max_length=64, verbose_name='Απόδειξη')),
                ('value_portion', models.CharField(choices=[('a', 'Εξόφληση συνολικής αξιας'), ('b', 'Δόσεις')], default='a', max_length=1, verbose_name='Τρόπος Πληρωμής')),
                ('value', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='Ποσό')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_manager.Order', verbose_name='Αριθμός Παραστατικου')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='orderitem',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_manager.Unit', verbose_name='Μονάδα Μέτρησης'),
        ),
    ]
