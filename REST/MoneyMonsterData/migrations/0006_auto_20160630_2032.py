# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyMonsterData', '0005_auto_20160629_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_completed',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
