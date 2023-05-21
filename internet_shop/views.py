from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product


def main(request):
    category_list = Category.objects.all()
    return render(request, 'internet_shop/main.html',
                  {'category_list': category_list})


def list_of_product(request, product_id: int):
    information_of_product = get_object_or_404(Product, id=product_id)
    context = {'information_of_product': information_of_product}
    return render(request, "internet_shop/list_of_product.html", context)


def list_of_category(request, category_id: int):
    information_of_category = get_object_or_404(Category, id=category_id)
    return render(request, 'internet_shop/list_of_category.html', {'information_of_category': information_of_category})

