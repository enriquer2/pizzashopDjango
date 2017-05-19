# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db.utils import IntegrityError
from social.backends.facebook import FacebookOAuth2
# from social.backends.google import GoogleOAuth2

from profiles.models import User


class CustomFacebookOAuth2(FacebookOAuth2):

    def do_auth(self, access_token, response=None, *args, **kwargs):
        result = super(CustomFacebookOAuth2, self).do_auth(access_token, response, *args, **kwargs)
        return result

# class CustomGoogleOAuth2(GoogleOAuth2):
#
#     def do_auth(self, access_token, response=None, *args, **kwargs):
#         result = super(CustomGoogleOAuth2, self).do_auth(access_token, response, *args, **kwargs)
#         if result:
#             try:
#                 new_user = Consumer.objects.create(user=result)
#                 new_user.register_with_google = True
#                 new_user.save()
#             except IntegrityError:
#                 pass
#         return result

