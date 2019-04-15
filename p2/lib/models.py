"""p2 lib models"""
from uuid import uuid4

from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models


class UUIDModel(models.Model):
    """Generic Model with a UUID as Primary key"""

    uuid = models.UUIDField(default=uuid4, primary_key=True)

    class Meta:

        abstract = True

class TagModel(models.Model):
    """Model which can be tagged and have pre-defined tag keys"""

    tags = JSONField(default=dict, blank=True, encoder=DjangoJSONEncoder)

    PREDEFINED_KEYS = []

    class Meta:

        abstract = True