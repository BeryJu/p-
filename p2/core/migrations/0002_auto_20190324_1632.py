# Generated by Django 2.1.7 on 2019-03-24 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p2_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basestorage',
            options={'permissions': (('use_storage', 'Use storage'),)},
        ),
    ]