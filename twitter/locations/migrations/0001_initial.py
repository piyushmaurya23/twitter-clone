# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('code', models.CharField(max_length=5)),
                ('parent_id', models.IntegerField()),
                ('location_type', models.CharField(max_length=10)),
            ],
        ),
    ]
