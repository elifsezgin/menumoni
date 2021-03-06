# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-13 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.IntegerField()),
                ('currency', models.CharField(choices=[(1, 'TRY'), (2, 'EUR'), (3, 'USD')], default='TRY', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='places')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Item')),
            ],
            options={
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('coordinates', models.CharField(max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Place'),
        ),
    ]
