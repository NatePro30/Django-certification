# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-06 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0019_auto_20170302_1427'),
        ('certificates', '0028_certificate_club_secondary'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatetype',
            name='players_club',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='certificatetype',
            name='players_club_clubs',
            field=models.ManyToManyField(related_name='cpc_certificate_types', to='clubs.Club'),
        ),
    ]
