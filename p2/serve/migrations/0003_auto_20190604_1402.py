# Generated by Django 2.2.1 on 2019-06-04 14:02

import uuid

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models

temp_rules = {}

def before_serverule_update(apps, schema_editor):
    """Remove ServeRules before upgrading, preventing an issue with pk."""
    ServeRule = apps.get_model("p2_serve", "ServeRule")
    for rule in ServeRule.objects.all():
        temp_rules[rule.name] = {
            'match': rule.match,
            'blob_query': rule.blob_query,
        }
    ServeRule.objects.all().delete()

def after_serverule_update(apps, schema_editor):
    """Create new rules"""
    ServeRule = apps.get_model("p2_serve", "ServeRule")
    from p2.serve.constants import TAG_SERVE_MATCH_PATH_RELATIVE
    for name, rule in temp_rules.items():
        ServeRule.objects.create(
            name=name,
            blob_query=rule['blob_query'],
            tags={
                TAG_SERVE_MATCH_PATH_RELATIVE: rule['match']
            }
        )

class Migration(migrations.Migration):

    dependencies = [
        ('p2_serve', '0002_remove_serverule_default'),
    ]

    operations = [
        migrations.RunPython(before_serverule_update),
        migrations.RemoveField(
            model_name='serverule',
            name='id',
        ),
        migrations.RemoveField(
            model_name='serverule',
            name='match',
        ),
        migrations.AddField(
            model_name='serverule',
            name='tags',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='serverule',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.RunPython(after_serverule_update),
    ]
