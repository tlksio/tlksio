# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0005_auto_20170402_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
