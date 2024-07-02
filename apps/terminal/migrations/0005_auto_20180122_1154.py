# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0004_session_remote_addr'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminal',
            name='command_storage',
            field=models.CharField(choices=[('default', 'default'), ('elk', 'elk')], default='default', max_length=128, verbose_name='Command storage'),
        ),
        migrations.AddField(
            model_name='terminal',
            name='replay_storage',
            field=models.CharField(default='default', max_length=128, verbose_name='Replay storage'),
        ),
    ]
