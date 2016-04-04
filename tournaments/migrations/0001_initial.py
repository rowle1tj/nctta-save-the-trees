# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 12:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_match', models.CharField(max_length=255)),
                ('active_team', models.CharField(choices=[(b'left', b'left'), (b'right', b'right')], max_length=255)),
                ('completed_datetime', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('owning_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('rating', models.CharField(blank=True, max_length=255, null=True)),
                ('order_id', models.IntegerField(blank=True, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('excel_document', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='teamplayer',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament'),
        ),
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament'),
        ),
        migrations.AddField(
            model_name='roster',
            name='doubles_partner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.TeamPlayer'),
        ),
        migrations.AddField(
            model_name='roster',
            name='left_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left_team', to='tournaments.Team'),
        ),
        migrations.AddField(
            model_name='roster',
            name='player1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='tournaments.TeamPlayer'),
        ),
        migrations.AddField(
            model_name='roster',
            name='player2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='tournaments.TeamPlayer'),
        ),
        migrations.AddField(
            model_name='roster',
            name='player3',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player3', to='tournaments.TeamPlayer'),
        ),
        migrations.AddField(
            model_name='roster',
            name='player4',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player4', to='tournaments.TeamPlayer'),
        ),
        migrations.AddField(
            model_name='roster',
            name='right_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_team', to='tournaments.Team'),
        ),
        migrations.AddField(
            model_name='roster',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament'),
        ),
    ]
