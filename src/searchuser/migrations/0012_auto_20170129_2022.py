# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 14:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchuser', '0011_auto_20170129_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearch',
            name='publish',
            field=models.DateField(default=datetime.date(2017, 1, 29)),
        ),
    ]
