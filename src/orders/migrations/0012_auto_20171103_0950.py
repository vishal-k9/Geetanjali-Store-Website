# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-03 09:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20171102_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='usercheckout',
            name='braintree_id',
        ),
    ]