# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 18:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0006_auto_20170402_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='vote_count',
        ),
    ]
