from django.urls import path, re_path
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('book_shelf/<pk>/', views.BookShelfListView.as_view(), name='book_shelf'),

    path('author/register', views.author_register, name='author_register'),


]



