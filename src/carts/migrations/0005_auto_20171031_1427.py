# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20171031_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(decimal_places=5, default=0.085, max_digits=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(decimal_places=2, default=25.0, max_digits=50),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=25.0, max_digits=50),
        ),
    ]
