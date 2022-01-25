from django.urls import path
from .import views

urlpatterns = [
    path('',views.user_login, name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('logout/',views.User_logout,name='logout'),
    path('library/',views.library,name='library'),
]