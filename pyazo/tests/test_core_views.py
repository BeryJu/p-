"""test core views"""
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase

from pyazo.models import Collection
from pyazo.tests.utils import test_auth


class CoreViewTests(TestCase):
    """Test core views"""

    def test_index(self):
        """Test default index page"""
        url = reverse('index')
        self.client.login(**test_auth())
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_paginator(self):
        """Test invalid paginator page"""
        url = reverse('index')
        self.client.login(**test_auth())
        response = self.client.get(url+'?page=3')
        self.assertEqual(response.status_code, 200)

    def test_index_collection(self):
        """Test valid collection"""
        url = reverse('index')
        self.client.login(**test_auth())
        Collection.objects.create(name='test', owner=User.objects.first())
        response = self.client.get(url+'?collection=test')
        self.assertEqual(response.status_code, 200)

    def test_index_collection_invalid(self):
        """Test invalid collection"""
        url = reverse('index')
        self.client.login(**test_auth())
        response = self.client.get(url+'?collection=aa')
        self.assertEqual(response.status_code, 404)
