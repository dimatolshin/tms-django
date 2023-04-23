from django.contrib import admin
from .models import Product, Category



class ProductInline(admin.TabularInline):
    model = Product
    extra = 1



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        ('Information', {'fields': ['category']}),
    ]
    list_display = ['name', 'category']
    list_filter = ['name', 'category']
    search_fields = ['name', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [ProductInline]