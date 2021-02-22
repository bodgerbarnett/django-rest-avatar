from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_avatar import serializers


User = get_user_model()


class TestSerializers(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('john@beatles.com', 'secret')

    def test_validate_file_too_big(self):
        # TODO how to upload images?
        data = {}
        serializer = serializers.AvatarSerializer(data=data)
        assert not serializer.is_valid()

    def tearDown(self):
        pass
