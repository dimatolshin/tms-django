from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login

from .forms import UserForm, NewUserForm
from .models import Category, Product, Order, OrderStatus


def index(request):
    return render(request, 'shop/index.html', {
        'categories': Category.objects.all(),
    })


def category_detail(request, category_id: int):
    return render(request, 'shop/category_detail.html', {
        'category': get_object_or_404(Category, id=category_id),
    })


def products_view(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/products.html', {
        'products': products, 'page_obj': page_obj,
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
def information_of_user(request: HttpRequest):
    orders = request.user.profile.orders.all().order_by('id').reverse()[:6]
    return render(request, 'shop/personal_account.html', {'orders': orders})


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
            messages.success(request, "You are change information ;)")
            return redirect('shop:information_of_user')
    else:
        form = UserForm(instance=request.user)
    return render(request, 'shop/edit_information.html', {'form': form})


@login_required()
def orders_complete(request):
    orders = request.user.profile.orders.exclude(status='INITIAL').order_by('-id')[:6]
    return render(request, 'shop/orders_complete.html', {'orders': orders})


@login_required()
def delete_one_order_entry(request):
    shopping_cart = request.user.profile.shopping_cart
    shopping_cart.order_entries.get(id=request.POST['objects_id']).delete()
    shopping_cart.save()
    messages.success(request, "Your product delete")
    return redirect('shop:my_basket')


@login_required()
def edit_count_order_entry(request):
    shopping_cart = request.user.profile.shopping_cart.order_entries.get(id=request.POST['objects_id'])
    shopping_cart.count = request.POST['objects_count']
    shopping_cart.save()
    return redirect('shop:my_basket')


@login_required()
def repeat_order(request):
    profile = request.user.profile
    shopping_cart = profile.shopping_cart
    shopping_cart.order_entries.all().delete()
    profile.shopping_cart.save()
    orders = request.user.profile.orders.get(id=request.POST['order_id'])
    for order in orders.order_entries.all():
        profile.shopping_cart.order_entries.create(product=order.product, count=order.count)
        profile.shopping_cart.save()
    profile.save()
    return redirect('shop:my_basket')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('shop:index')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "registration/register.html", context={"form": form})


def search_products(request):
    products = Product.objects.filter(name__icontains=request.POST['search'])
    return render(request, 'shop/search.html', {'products': products})

## у input text есть values {{в котором можно указать то что будет в строке текст}}
