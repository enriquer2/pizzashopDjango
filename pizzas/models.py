from __future__ import unicode_literals

from uuid import uuid4

from decimal import Decimal

from django.conf import settings
# from django.contrib.auth.models import User #adadad
# from profiles.models import User

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# Previous version of Python    
#    def __unicode__(self):
#        return self.name


def pizzas_pictures_path(instance, filename):
    ext = filename.split('.')[-1]
    # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return '{0}/{1}'.format('pizzas', filename)


class Pizza(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    ingredients = models.ManyToManyField("pizzas.Ingredient", verbose_name=_("Ingredients"), related_name="pizzas")
    image = models.ImageField(verbose_name=_("Image"), upload_to=pizzas_pictures_path, blank=True, null=True)

    @property
    def price(self):
        price = Decimal(0.0)
        for ingredient in self.ingredients.all():
            price += ingredient.price
        return price * Decimal(1.5)

# Previous version of Python
#    def __unicode__(self):
#        return self.name

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(verbose_name=_("Comment text"), max_length=140)
    created = models.DateTimeField(verbose_name=_("Created"), auto_now_add=True)
    score = models.IntegerField(verbose_name=_("Score"), default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), related_name="comments", related_query_name="comment", null=True)
    pizza = models.ForeignKey(Pizza, verbose_name=_("Pizza"), related_name="comments", related_query_name="comment")

    def save(self, *args, **kwargs):
        if self.score > 5:
            self.score = 5
        elif self.score < 0:
            self.score = 0
        super(Comment, self).save(*args, **kwargs)

# Previous version of Python
#    def __unicode__(self):
#        return self.user.username + " - " + self.text

    def __str__(self):
        return self.user.username + " - " + self.text

    @property
    def username(self):
        return self.user.username