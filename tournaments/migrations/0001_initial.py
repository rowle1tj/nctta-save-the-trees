# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round_match', models.CharField(max_length=255)),
                ('active_team', models.CharField(max_length=255, choices=[(b'left', b'left'), (b'right', b'right')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('owning_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255, null=True, blank=True)),
                ('order_id', models.IntegerField(null=True, blank=True)),
                ('team', models.ForeignKey(to='tournaments.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('excel_document', models.FileField(null=True, upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='teamplayer',
            name='tournament',
            field=models.ForeignKey(to='tournaments.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(to='tournaments.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='roster',
            name='left_team',
            field=models.ForeignKey(related_name='left_team', to='tournaments.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='roster',
            name='right_team',
            field=models.ForeignKey(related_name='right_team', to='tournaments.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='roster',
            name='tournament',
            field=models.ForeignKey(to='tournaments.Tournament'),
            preserve_default=True,
        ),
    ]
