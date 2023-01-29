from django.contrib import admin

from .models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "category", "price", "created_at", "updated_at"]
    list_filter = ["category", "created_at", "updated_at"]
    list_editable = ["price"]
    prepopulated_fields = {"slug": ("name",)}
