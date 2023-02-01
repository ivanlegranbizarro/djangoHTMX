from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = "core"

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("shop/", views.shop, name="shop"),
    path("products/<slug:slug>/", views.products_detail, name="products_detail"),
    path(
        "category/<slug:slug>/", views.products_by_category, name="products_by_category"
    ),
    path("signup/", views.signup, name="signup"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("my-account/", views.my_account, name="my_account"),
    path("my-account/edit/", views.edit_my_account, name="edit_my_account"),
]
