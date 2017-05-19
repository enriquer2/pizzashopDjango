# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from restless.dj import DjangoResource
from restless.exceptions import NotFound
from restless.preparers import FieldsPreparer

from pizzas.models import Pizza


class PizzaResource(DjangoResource):
    preparer = FieldsPreparer({
        'id': 'pk',
        'name': 'name'
    })

    def is_authenticated(self):
        return True

    def detail(self, pk):
        try:
            pizza = Pizza.objects.get(pk=pk)
        except Pizza.DoesNotExist:
            raise NotFound
        return pizza

    def list(self):
        return Pizza.objects.all()


class IngredientResource(DjangoResource):
    preparer = FieldsPreparer({
        'id': 'pk',
        'name': 'name'
    })