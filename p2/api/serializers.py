"""p2 API Serializers"""
from django.contrib.auth.models import User
from rest_framework.serializers import (HyperlinkedModelSerializer,
                                        ModelSerializer, ReadOnlyField)

from p2.lib.models import TagModel


class TagModelSerializer(ModelSerializer):
    """TagModel base serializer"""

    predefined_keys = ReadOnlyField(source='PREDEFINED_KEYS')

    class Meta:

        model = TagModel
        fields = '__all__'

class UserSerializer(HyperlinkedModelSerializer):
    """User Serializer"""

    class Meta:

        model = User
        fields = '__all__'