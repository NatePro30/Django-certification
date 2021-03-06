# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 13:33
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0026_club_bilingual'),
        ('users', '0012_auto_20170403_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='home_club_alternate_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alt1_users', to='clubs.Club'),
        ),
        migrations.AddField(
            model_name='user',
            name='home_club_alternate_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alt2_users', to='clubs.Club'),
        ),
    ]
