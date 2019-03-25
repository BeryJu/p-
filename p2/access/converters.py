"""p2 access URL converters"""
from django.urls.converters import StringConverter


class EverythingButSlashConverter(StringConverter):
    """Match everything but slash"""

    regex = '/([^/]+)/?(.*)'
