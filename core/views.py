from django.db.models import Q
from django.shortcuts import render

from products.models import Category, Product

# Create your views here.


def signup(request):
    return render(request, "core/signup.html")


def login(request):
    return render(request, "core/login.html")


def frontpage(request):
    products = Product.objects.all()[0:8]
    return render(request, "core/frontpage.html", {"products": products})


def shop(request):
    products = Product.objects.all()
    query = request.GET.get("query")
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    return render(request, "core/shop.html", {"products": products})


def get_categories(request):
    categories = Category.objects.all()
    return {"all_categories": categories}


def products_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    return render(
        request,
        "core/shop.html",
        {"products": products},
    )


def products_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, "core/products_detail.html", {"product": product})
