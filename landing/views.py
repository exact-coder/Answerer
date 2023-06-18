from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"landing/pages/home.html")

def pricing(request):
    return render(request,"landing/pages/pricing.html")

def blog(request):
    return render(request,"landing/pages/blog.html")

def contact(request):
    return render(request,"landing/pages/contact.html")

def service(request):
    return render(request,"landing/pages/service.html")

