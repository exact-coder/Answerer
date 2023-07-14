from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

# Create your views here.



@login_required(login_url="auth_login")
def dashboard(request):
    return render(request,'authorization/pages/dashboard.html')

@login_required(login_url="auth_login")
def user_profile(request):
    context = {}
    form = ProfileForm()
    return render(request,'authorization/pages/user_profile.html')

@login_required(login_url="auth_login")
def user_profile_edit(request):
    return render(request,'authorization/pages/user_profile_edit.html')
