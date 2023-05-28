import profile

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.cache import cache_page

from .models import Category, Product, Order, OrderEntry ,OrderStatus


def index(request):
    return render(request, 'shop/index.html', {
        'categories': Category.objects.all(),
    })


def category_detail(request, category_id: int):
    return render(request, 'shop/category_detail.html', {
        'category': get_object_or_404(Category, id=category_id),
    })


def products_view(request):
    return render(request, 'shop/products.html', {
        'products': Product.objects.all(),
    })


def product_detail(request, product_id: int):
    return render(request, 'shop/product_detail.html', {
        'product': get_object_or_404(Product, id=product_id),
    })


@login_required()
def add_to_cart(request):
    profile = request.user.profile
    if not profile.shopping_cart:
        profile.shopping_cart = Order(profile=request.user.profile)  # т.к связь one to one нужен такой конструктор , для связи где есть релайтет нейм на стороне мени можно обращаться через .create
        profile.shopping_cart.save()

    assert request.method == "POST"
    product_id = request.POST['product_id']
    product = get_object_or_404(Product, id=product_id)

    order_entry = profile.shopping_cart.order_entries.filter(product=product).first()
    if not order_entry:
        order_entry = profile.shopping_cart.order_entries.create(product=product, count=0)
    order_entry.count += 1
    order_entry.save()

    return redirect('shop:product_detail', product_id)


@login_required()
def my_basket(request):
    profile = request.user.profile
    if not profile.shopping_cart:
        profile.shopping_cart = Order(profile=request.user.profile)
        profile.shopping_cart.save()
    order_entry = OrderEntry.objects.all()
    all_sum = 0
    for objects in order_entry:
        count = objects.count
        price = objects.product.price
        total = count * price
        all_sum += total
    return render(request, 'shop/my_basket.html', {'order_entry': order_entry, 'all_sum': all_sum})


def delete_order_entry(request):
    assert request.method == "POST"
    order=request.user.profile.shopping_cart
    order_entry=OrderEntry.objects.filter(order=order)
    order_entry.delete()
    return redirect('shop:my_basket')

def checkout(request):
    profile = request.user.profile
    order = profile.shopping_cart
    order.status = OrderStatus.COMPLETED
    order.save()
    profile.shopping_cart = Order.objects.create(profile=profile)
    profile.save()
    redirect('shop:my_basket')



