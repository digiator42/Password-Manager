from django.urls import path
from . import views

urlpatterns = [
    path('', views.password_list, name='password_list'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.auth_logout, name='logout'),
    path('add/', views.add_password, name='add_password'),
    path('view/<int:pk>/', views.view_password, name='view_password'),
    path('delete/<int:pk>/', views.delete_password, name='delete_password'),
    path('accounts/profile/', views.profile, name='profile'),
]