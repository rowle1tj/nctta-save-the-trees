# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_auto_20150208_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roster',
            name='left_team',
            field=models.ForeignKey(related_name='left_team', blank=True, to='tournaments.Team', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roster',
            name='right_team',
            field=models.ForeignKey(related_name='right_team', blank=True, to='tournaments.Team', null=True),
            preserve_default=True,
        ),
    ]
