# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-08 17:31
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('neutralvendor', '0003_auto_20181208_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='check1',
            field=otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '560'], [2, '522'], [3, '700']], null=True),
        ),
    ]