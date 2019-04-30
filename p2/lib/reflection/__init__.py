"""p2 lib reflection utilities"""
from importlib import import_module


def class_to_path(cls):
    """Turn Class (Class or instance) into module path"""
    return '%s.%s' % (cls.__module__, cls.__name__)


def path_to_class(path):
    """Import module and return class"""
    if not path:
        return None
    parts = path.split('.')
    package = '.'.join(parts[:-1])
    _class = getattr(import_module(package), parts[-1])
    return _class


def get_apps():
    """Get list of all p2 apps"""
    from django.apps.registry import apps
    for _app in apps.get_app_configs():
        if _app.name.startswith('p2'):
            yield _app


def app(name):
    """Return true if app with `name` is enabled"""
    from django.conf import settings
    return name in settings.INSTALLED_APPS
