# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchuser', '0010_auto_20170129_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearch',
            name='publish',
            field=models.DateField(),
        ),
    ]
