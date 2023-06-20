from django.urls import path
from . import views



urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views.auth_login,name='auth_login'),
    path('register/',views.auth_register,name='auth_register'),
]

