# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-17 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0019_auto_20170302_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='tender_method_guid',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
