# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchuser', '0012_auto_20170129_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearch',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
