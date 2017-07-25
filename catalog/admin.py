# coding=utf-8

from django.contrib import admin

from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    """Configure admin for category class"""
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']


class ProductAdmin(admin.ModelAdmin):
    """Configure admin for category class"""
    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
