# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 20:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_contact_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]