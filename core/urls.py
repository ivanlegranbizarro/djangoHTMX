from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("shop/", views.shop, name="shop"),
    path("products/<slug:slug>/", views.products_detail, name="products_detail"),
]
