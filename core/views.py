from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from products.models import Category, Product

from .forms import SignUpForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "core/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")


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


@login_required
def my_account(request):
    return render(request, "core/my_account.html")


@login_required
def edit_my_account(request):
    return render(request, "core/edit_my_account.html")
