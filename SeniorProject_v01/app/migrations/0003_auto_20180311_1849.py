# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 01:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180311_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='troop',
            old_name='troop_number',
            new_name='number',
        ),
    ]
