from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.main, name='main'),
    path('<int:article_id>', views.title, name='title'),
    path('<int:article_id>/like', views.like, name='like'),
]
