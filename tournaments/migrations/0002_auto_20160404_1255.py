# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roster',
            name='completed_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
