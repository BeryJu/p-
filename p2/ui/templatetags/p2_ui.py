"""p2 ui templatetags"""
import json

from django import template
from django.db.models import Model

from p2.lib.reflection import path_to_class

register = template.Library()


@register.simple_tag(takes_context=True)
def model_app(context, expected=None):
    """Check if current view's model is the same as expected. Return "active" if both match"""
    view = context.get('view', None)
    app = None
    if hasattr(view, 'model'):
        app = view.model._meta.app_label
    return "active" if app == expected else ""

@register.filter
def model_verbose_name(model):
    """Return model's verbose_name"""
    if isinstance(model, Model):
        model = model.__class__
    return model._meta.verbose_name

@register.filter
def get_attribute(blob, path):
    """Access blob.attributes but allow keys like 'site:bytes"""
    return blob.attributes.get(path_to_class(path))


@register.filter('startswith')
def startswith(text, starts):
    """Simple wrapper for str.startswith"""
    if isinstance(text, str):
        return text.startswith(starts)
    return False

@register.filter('json')
def json_pretty(obj):
    """Convert obj into pretty-printed JSON"""
    return json.dumps(obj, indent=4, sort_keys=True)
