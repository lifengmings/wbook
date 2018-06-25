from django.urls import path, re_path
from . import views

app_name = 'author'
urlpatterns = [
    path('index/', views.index, name='index'),

    path('my_book_list', views.my_book_list, name='my_book_list'),
    path('create_book/', views.create_book, name='book_create'),
    path('add_new_volume/<int:pk>/', views.add_new_volume, name='add_new_volume'),
    path('add_new_volume_modal/<int:pk>/', views.add_new_volume_modal, name='add_new_volume_modal'),
    path('update_book/<int:pk>/', views.update_book, name='update_book'),


]
