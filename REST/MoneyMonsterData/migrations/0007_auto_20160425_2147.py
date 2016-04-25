# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-25 21:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyMonsterData', '0006_haps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haps',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]