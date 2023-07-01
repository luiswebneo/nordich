# Criando as views aplicativo core

from django.shortcuts import render

from product.models import Product, Category


def frontpage(request):
    products = Product.objects.all()[0:8]

    return render(request, 'core/frontpage.html', {'products': products})

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories, 
        'products': products
    }


    return render(request, 'core/shop.html', context)