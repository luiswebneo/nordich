from django.contrib import admin

from .models import Category, Product
# Registrando os models do aplicativo no painel admin

admin.site.register(Category)
admin.site.register(Product)
