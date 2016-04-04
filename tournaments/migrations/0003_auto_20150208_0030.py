# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_auto_20150208_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roster',
            name='tournament',
            field=models.ForeignKey(blank=True, to='tournaments.Tournament', null=True),
            preserve_default=True,
        ),
    ]
