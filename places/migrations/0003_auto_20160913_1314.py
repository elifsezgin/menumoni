# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-13 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_place_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[(1, 'TRY'), (2, 'EUR'), (3, 'USD')], default='TRY', max_length=255),
        ),
    ]