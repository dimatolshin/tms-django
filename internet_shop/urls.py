from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.category_detail, name='category_detail'),
    path('products/', views.products_view, name='products'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('my_basket/', views.my_basket, name='my_basket'),
    path('delete_order_entry/',views.delete_order_entry,name='delete_order_entry'),
    path('checkout/',views.checkout,name='checkout'),
]
