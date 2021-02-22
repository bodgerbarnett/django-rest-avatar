#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_avatar import models


User = get_user_model()


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('john@beatles.com', 'secret')

    def test_set_primary(self):
        avatar = models.Avatar.objects.create(user=self.user)
        avatar.set_primary()
        self.assertTrue(avatar.is_primary)

    def tearDown(self):
        pass
