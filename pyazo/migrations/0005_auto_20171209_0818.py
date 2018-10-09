# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-09 08:18
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyazo', '0004_auto_20171002_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]