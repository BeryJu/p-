"""S3 Unittest utils"""
from uuid import uuid4

import boto3
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from guardian.shortcuts import assign_perm

from p2.api.models import APIKey
from p2.core.models import Volume
from p2.core.tests.utils import get_test_storage
from p2.s3.constants import TAG_S3_DEFAULT_STORAGE


class S3TestCase(LiveServerTestCase):
    """Unittest utils-related operations"""

    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(
            username='p2_unittest',
            email='test@test.test',
            password=uuid4().hex)
        self.access_key, _ = APIKey.objects.get_or_create(
            user=self.user)
        self.storage = get_test_storage()
        self.storage.tags[TAG_S3_DEFAULT_STORAGE] = True
        self.storage.save()
        self.volume = Volume.objects.create(
            name='test-1', storage=self.storage)
        assign_perm('p2_core.use_volume', self.user, self.volume)
        assign_perm('p2_core.add_blob', self.user)
        session = boto3.session.Session()
        self.boto3 = session.client(
            service_name='s3',
            aws_access_key_id=self.access_key.access_key,
            aws_secret_access_key=self.access_key.secret_key,
            endpoint_url=self.live_server_url,
        )
