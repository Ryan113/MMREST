# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-11 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyMonsterData', '0003_video_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='thumbnail',
            new_name='thumbnailUrl',
        ),
    ]
