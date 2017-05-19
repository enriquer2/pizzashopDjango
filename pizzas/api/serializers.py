# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from pizzas.models import Ingredient, Pizza, Comment

import json

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    class Meta:
        model = Comment
        fields = "__all__"
        
class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Pizza
        fields = "__all__"

    def create(self, validated_data):
        # Since validated_data doesn't contain the ingredients
        # because of the form/multipar format used in the post request
        # we have to extract them from the initial_data inside self
        # and then convert it to json

        # We must also remove ingredients and comments
        # to avoid validation errors due to wrong format
        ingredients_data = self.initial_data['ingredients']
        ingredients_data = json.loads(ingredients_data)
        ingridients_parsed = list(map(lambda c : json.loads(c),ingredients_data))
        validated_data.pop('ingredients')
        validated_data.pop('comments')
        pizza = Pizza.objects.create(**validated_data)
        for ingredient in ingridients_parsed:
            p = Ingredient.objects.get(name=ingredient["name"])
            pizza.ingredients.add(p)
        return pizza


