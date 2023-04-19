from django.urls import path

from . import views

app_name = 'internet_shop'
urlpatterns = [
    path('', views.main, name='main'),
    path('<int:product_id>/product', views.list_of_product, name='information_of_product'),
    path('<int:category_id>/category', views.list_of_category, name='information_of_category')
]
