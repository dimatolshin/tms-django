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
    path('delete_order_entry/', views.delete_order_entry, name='delete_order_entry'),
    path('checkout/', views.checkout, name='checkout'),
    path('personal_account/', views.information_of_user, name='information_of_user'),
    path('edit_information/', views.edit_information, name='edit_information'),
    path('orders_complete/', views.orders_complete, name='orders_complete'),
    path('delete_one_order_entry/', views.delete_one_order_entry, name='delete_one_order_entry'),
    path('edit_count_order_entry/', views.edit_count_order_entry, name="edit_count_order_entry"),
    path('repeat_order', views.repeat_order, name='repeat_order'),
    path("register", views.register_request, name="register"),
]
