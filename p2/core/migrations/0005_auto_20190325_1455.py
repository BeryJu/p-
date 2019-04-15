# Generated by Django 2.1.7 on 2019-03-25 14:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p2_core', '0004_auto_20190324_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basestorage',
            name='values',
        ),
        migrations.AddField(
            model_name='basestorage',
            name='tags',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='volume',
            name='tags',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]