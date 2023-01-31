from django.urls import path

from . import views

app_name = "cart"

urlpatterns = [
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path(
        "substract-to-cart/<int:product_id>/",
        views.substract_to_cart,
        name="substract_to_cart",
    ),
    path("", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
]
