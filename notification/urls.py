from django.urls import path
from notification import views


app_name = 'notification'
urlpatterns = [
    path('updatemsg/', views.updatemsg, name='updatemsg'),
    path('set_read/', views.set_read, name='set_read'),
]
