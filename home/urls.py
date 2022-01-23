from django.urls import path
from .import views

urlpatterns = [
    path('',views.user_login, name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home')
]