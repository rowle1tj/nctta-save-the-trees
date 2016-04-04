# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nctta_org', '0002_auto_20160404_1310'),
        ('tournaments', '0003_auto_20160404_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nctta_org.College'),
        ),
    ]