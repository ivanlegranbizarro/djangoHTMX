from django.shortcuts import render

from products.models import Category, Product

# Create your views here.


def frontpage(request):
    products = Product.objects.all()[0:8]
    return render(request, "core/frontpage.html", {"products": products})


def shop(request):
    products = Product.objects.all()
    return render(request, "core/shop.html", {"products": products})


def get_categories(request):
    categories = Category.objects.all()
    return {"all_categories": categories}


def products_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, "core/products_detail.html", {"product": product})
