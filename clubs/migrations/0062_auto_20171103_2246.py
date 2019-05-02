# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-04 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0061_remove_club_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='hide_daily_fees',
            field=models.BooleanField(default=False, help_text='If you want to hide the daily fees menu from the hamburger menu for this club'),
        ),
        migrations.AlterField(
            model_name='club',
            name='daily_fee_location',
            field=models.BooleanField(default=False, help_text='NOTE: As per Brendan, also accounts for several other things in page scaffolding, and is therefore "needed" for building out pages for now.'),
        ),
    ]