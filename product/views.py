from django.shortcuts import render

# Criando as views do app product

def product(request):
    return render(request, 'product/product.html')