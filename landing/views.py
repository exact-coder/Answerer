from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"landing/pages/home.html")

def about(request):
    return render(request,"landing/pages/about.html")

def blog(request):
    return render(request,"landing/pages/blog.html")

def contact(request):
    return render(request,"landing/pages/contact.html")

def service(request):
    return render(request,"landing/pages/service.html")

