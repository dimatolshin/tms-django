from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product


def main(request):
    list_products = Product.objects.all()
    context = {'list_products': list_products}
    return render(request, 'shop/main.html', context)
