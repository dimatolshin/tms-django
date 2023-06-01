import profile

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.contrib import messages

from .forms import UserForm
from .models import Category, Product, Order, OrderEntry, OrderStatus


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
        profile.shopping_cart = Order(
            profile=request.user.profile)  # т.к связь one to one нужен такой конструктор , для связи где есть релайтет нейм на стороне мени можно обращаться через .create
        profile.shopping_cart.save()
        profile.save()

    assert request.method == "POST"
    product_id = request.POST['product_id']
    product = get_object_or_404(Product, id=product_id)

    order_entry = profile.shopping_cart.order_entries.filter(product=product).first()
    if not order_entry:
        order_entry = profile.shopping_cart.order_entries.create(product=product, count=0)
    order_entry.count += 1
    order_entry.save()
    messages.success(request, 'You are adding product in the basket')
    return redirect('shop:product_detail', product_id)


@login_required()
def my_basket(request):
    profile = request.user.profile
    if not profile.shopping_cart:
        profile.shopping_cart = Order(profile=request.user.profile)
        profile.shopping_cart.save()
        profile.save()
    order_entry = profile.shopping_cart.order_entries.all()
    all_sum = 0
    for objects in order_entry:
        count = objects.count
        price = objects.product.price
        total = count * price
        all_sum += total
    return render(request, 'shop/my_basket.html', {'order_entry': order_entry, 'all_sum': all_sum})


def delete_order_entry(request):
    assert request.method == "POST"
    order = request.user.profile.shopping_cart
    order.order_entries.all().delete()
    order.save()
    messages.info(request, "You are cleaning basket right now!")
    return redirect('shop:my_basket')


def checkout(request):
    profile = request.user.profile
    order = profile.shopping_cart
    order.status = OrderStatus.COMPLETED
    order.save()
    profile.shopping_cart = Order.objects.create(profile=profile)
    profile.save()
    messages.success(request, 'Сongratulations your order is paid')
    return redirect('shop:my_basket')


@login_required()
def information_of_user(request: HttpRequest, user_id: int):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'shop/personal_account.html', {'user': user})

@login_required()
def edit_information(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = request.user
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request,"You are change information ;)")
            return redirect('shop:information_of_user', user.id)
    else:
        form = UserForm()
        form.username=request.user.username
    return render(request, 'shop/edit_information.html', {'form': form})


## у input text есть values {{в котором можно указать то что будет в строке текст}}