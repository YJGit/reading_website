# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20160728_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]