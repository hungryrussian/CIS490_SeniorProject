# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-03 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20180602_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtype',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
