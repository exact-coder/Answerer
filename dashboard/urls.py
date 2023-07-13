from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('profile/',views.user_profile,name='user_profile'),
    path('profile/edit/',views.user_profile_edit,name='user_profile_edit'),
]
