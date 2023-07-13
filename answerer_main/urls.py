
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("landing.urls")),
    path('answerer/auth/',include("authorization.urls")),
    path('answerer/dashboard/',include("dashboard.urls")),
]
