# Generated by Django 2.2.1 on 2019-05-15 09:51

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p2_log', '0005_auto_20190430_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logadaptor',
            name='tags',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]