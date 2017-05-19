# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from pizzas.api.serializers import IngredientSerializer, PizzaSerializer, CommentSerializer
from pizzas.models import Ingredient, Pizza, Comment


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = []

    # def get_queryset(self):
    #     name = self.request.GET.get("name", "")
    #     if name != "":
    #         return Ingredient.objects.filter(name__icontains=name)
    #     return Ingredient.objects.all()


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = []

    # @detail_route()
    # def comments(self, pk):
    #      comments = Comment.objects.filter(pizza__pk=pk)
    #      serializer = CommentSerializer(comments, many=True)
    #      return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        #IsAuthenticated
    ]
