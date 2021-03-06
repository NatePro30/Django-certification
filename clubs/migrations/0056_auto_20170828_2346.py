# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-29 03:46
# flake8: noqa
from __future__ import unicode_literals

import clublink.base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0055_auto_20170823_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='academy_logo',
            field=models.FileField(blank=True, null=True, upload_to=clublink.base.utils.RandomizedUploadPath('academy_logos')),
        ),
        migrations.AlterField(
            model_name='club',
            name='dark_logo',
            field=models.FileField(blank=True, null=True, upload_to=clublink.base.utils.RandomizedUploadPath('dark_logos')),
        ),
    ]
