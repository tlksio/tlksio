# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0012_talk_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='thumbnail',
            field=models.URLField(blank=True, null=True, verbose_name='video thumbnail'),
        ),
    ]
