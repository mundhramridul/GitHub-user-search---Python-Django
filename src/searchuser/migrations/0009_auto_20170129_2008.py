# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchuser', '0008_auto_20170129_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearch',
            name='timestamp',
            field=models.DateField(),
        ),
    ]