# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-28 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutout_extension', '0013_auto_20180927_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cutoutquery',
            name='plot_units',
            field=models.CharField(choices=[('fits', 'FITS')], default=None, max_length=1),
        ),
    ]