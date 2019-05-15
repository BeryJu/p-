# Generated by Django 2.2 on 2019-04-23 10:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p2_core', '0008_auto_20190403_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basestorage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='blob',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='volume',
            name='tags',
        ),
        migrations.AddField(
            model_name='basestorage',
            name='tags',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='blob',
            name='tags',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='volume',
            name='tags',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
