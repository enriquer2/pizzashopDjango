from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .managers import UserManager

# Create your models here.


def user_username_check(text, uids):
    if text in uids:
        return False
    return not User.objects.filter(username=text).exists()


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("Email address"), unique=True)
    username = models.CharField(_("Username"), max_length=254, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=100, blank=True)
    phone = models.CharField(verbose_name=_("Phone"), max_length=30, blank=True)
    city = models.CharField(verbose_name=_("City"), max_length=100, blank=True)
    birthday = models.DateField(verbose_name=_("Birthday"), null=True, blank=True)
    is_staff = models.BooleanField(
        _("is staff"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site.")
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_("Designates whether this user should be treated as active. Unselect this instead of "
                    "deleting accounts.")
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

    @property
    def full_name(self):
        if self.name != '':
            return self.name
        return self.username

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __unicode__(self):
        return self.full_name




