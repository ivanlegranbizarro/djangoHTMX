from django.shortcuts import render

from products.models import Category, Product

# Create your views here.


def frontpage(request):
    products = Product.objects.all()[0:8]
    return render(request, "core/frontpage.html", {"products": products})
