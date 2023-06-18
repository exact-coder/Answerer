from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("pricing/",pricing,name="pricing"),
    path("blog/",blog,name="blog"),
    path("contact/",contact,name="contact"),
    path("service/",service,name="service"),
]
