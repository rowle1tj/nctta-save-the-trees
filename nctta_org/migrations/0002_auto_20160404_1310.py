# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nctta_org', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='school',
            new_name='college',
        ),
    ]
