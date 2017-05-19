# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError, PermissionDenied
from django.db.models import Count
from django.utils.translation import ugettext
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from profiles.api import permissions
from profiles.api.serializers import SignUpSerializer, UserSerializer, UserPictureSerializer
from profiles.models import User


class SignUpResource(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (permissions.IsAuthenticatedOrCreate,)


class UserResource(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_object(self):
        if self.kwargs.get('pk', None) == 'me':
            self.kwargs['pk'] = self.request.user.pk
        if (self.action == 'update' or self.action == 'partial_update') and int(self.kwargs['pk']) != self.request.user.pk:
            raise PermissionDenied
        return super(UserResource, self).get_object()

    @list_route(methods=['get'])
    def ranking(self, request):
        users = User.objects.all().annotate(purchases_count=Count('purchase')).order_by('-purchases_count')

        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    @list_route(methods=['post'])
    def picture(self, request):
        serializer = UserPictureSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @list_route(methods=['post'])
    def change_password(self, request):
        if "old_password" not in request.data:
            return Response(ugettext("Old password is mandatory"), status=status.HTTP_400_BAD_REQUEST)
        elif "password" not in request.data:
            return Response(ugettext("Password is mandatory"), status=status.HTTP_400_BAD_REQUEST)
        old_password = request.data["old_password"]
        password = request.data["password"]

        if not request.user.check_password(old_password):
            return Response(ugettext("Cannot change password"), status=status.HTTP_400_BAD_REQUEST)
        try:
            validate_password(password)
        except ValidationError as e:
            return Response(e.messages[0], status=status.HTTP_400_BAD_REQUEST)
        request.user.set_password(password)
        request.user.save()
        return Response(ugettext("Password changed"))


