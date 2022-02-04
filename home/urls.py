
from django.urls import path
from .import views

urlpatterns = [
    path('',views.user_login, name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('logout/',views.User_logout,name='logout'),
    path('library/',views.library,name='library'),
    path('add_books/',views.add_books,name='add_books'),
    path('edit_books/<int:id>/',views.edit_books,name='edit_books'),
    path('delete_books/<int:id>/', views.delete_books, name='delete_books'),
    path('list_books/',views.list_books, name='list_books'),
]