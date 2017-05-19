# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from profiles.models import User
from django.contrib.auth.hashers import check_password


class EmailAuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email__iexact=username)
            if check_password(password, user.password):
                return user
            else:
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None