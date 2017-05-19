from django.contrib import admin

# Register your models here.
from pizzas.models import Ingredient, Pizza, Comment

admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Comment)
