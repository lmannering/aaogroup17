# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-21 03:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cutout_extension', '0016_auto_20181021_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cutoutquery',
            old_name='output_units',
            new_name='output_type',
        ),
    ]
