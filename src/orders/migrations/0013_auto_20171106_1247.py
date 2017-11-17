# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-06 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20171103_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
    ]
