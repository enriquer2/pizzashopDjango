# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from pizzas.api.resources import PizzaResource

urlpatterns = [
    url(r'pizzas/', include(PizzaResource.urls()))
]