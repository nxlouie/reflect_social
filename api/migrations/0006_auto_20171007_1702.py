# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171007_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interactiontag',
            name='id',
        ),
        migrations.AlterField(
            model_name='interactiontag',
            name='tag_name',
            field=models.IntegerField(choices=[(1, 'Career'), (2, 'Social'), (3, 'Family'), (4, 'Dating'), (5, 'Obligation'), (6, 'Worthwhile'), (7, 'Time Waste')], primary_key=True, serialize=False),
        ),
    ]
