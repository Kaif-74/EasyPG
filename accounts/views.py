from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import OwnerRegistrationForm
from .models import OwnerProfile
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = OwnerRegistrationForm(request.POST)
        if form.is_valid():
            # Create the User
            user = User.objects.create_user(
                username=form.cleaned_data['email'], # We use email as username
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Create the Owner Profile
            OwnerProfile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                mobile_number=form.cleaned_data['mobile_number']
            )
            messages.success(request, "Registration successful! Please login.")
            return redirect('login')
    else:
        form = OwnerRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') # We will change this to dashboard later
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')