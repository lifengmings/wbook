from django.urls import path, re_path
from . import views

urlpatterns = [
    path('info/<int:pk>', views.book_detail, name='book_info'),
    path('chapter/<int:pk>/', views.read_page, name='chapter'),

    re_path('classify/(?P<name>[\w]+)/', views.classify_x, name='classify_x'),

    path('join_bookshelf/', views.join_bookshelf, name='join_bookshelf'),
    path('ranking/', views.click_rank, name='ranking'),
]