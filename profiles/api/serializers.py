# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from profiles.models import User


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password')
        write_only_fields = ('password',)

    @staticmethod
    def validate_password(value):
        value = make_password(value)
        return value

    def save(self, **kwargs):
        user = super(SignUpSerializer, self).save(**kwargs)
        return user


class UserPictureSerializer(serializers.ModelSerializer):

    avatar_picture = serializers.ImageField()

    class Meta:
        model = User
        fields = ['avatar_picture']


class UserSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(write_only=True)
    avatar_picture = serializers.SerializerMethodField()
    last_location = serializers.SerializerMethodField()
    num_purchases = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id", "name", "phone", "city", "birthday", "username", "email", "password", "old_password"
        ]
        extra_kwargs = {'password': {'write_only': True}}

    @staticmethod
    def validate_password(value):
        value = make_password(value)
        return value

    def get_num_purchases(self, obj):
        return obj.num_purchases

    def validate_old_password(self, value):
        if self.instance and not self.instance.check_password(value):
            raise serializers.ValidationError("Bad old password")
        return value