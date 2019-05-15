# Generated by Django 2.2 on 2019-04-30 19:36

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2_log', '0003_auto_20190415_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logadaptor',
            options={'verbose_name': 'Log Adaptor', 'verbose_name_plural': 'Log Adaptors'},
        ),
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': 'Log Record', 'verbose_name_plural': 'Log Records'},
        ),
        migrations.RemoveField(
            model_name='logadaptor',
            name='options',
        ),
        migrations.AddField(
            model_name='logadaptor',
            name='controller_path',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logadaptor',
            name='name',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logadaptor',
            name='tags',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.DeleteModel(
            name='DatabaseLogAdaptor',
        ),
    ]
