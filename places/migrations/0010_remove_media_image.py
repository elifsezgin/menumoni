# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-13 10:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20160913_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='image',
        ),
    ]
