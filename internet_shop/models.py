from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.views import View


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')

    def __str__(self):
        return self.name


class OrderEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
    count = models.IntegerField(default=0)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_entries')

    def __str__(self):
        return f'{self.product} - {self.count}'

    @property
    def price(self):
        return self.count * self.product.price


class OrderStatus(models.TextChoices):
    INITIAL = 'INITIAL',
    COMPLETED = 'COMPLETED',
    DELIVERED = 'DELIVERED',


class Order(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.INITIAL)

    def __str__(self):
        return f'id:{self.id} - {self.profile} - {self.status}'

    @property
    def price(self):
        return sum(order_entry.price for order_entry in self.order_entries.all())

    @property
    def count(self):
        return sum(order_entry.count for order_entry in self.order_entries.all())


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    shopping_cart = models.OneToOneField(Order, on_delete=models.SET_NULL,
                                         null=True, blank=True, related_name='+')

    def __str__(self):
        return str(self.user)




