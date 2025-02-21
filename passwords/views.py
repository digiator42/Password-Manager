from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PasswordEntry
from .serializer import PasswordFormSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

@login_required
def password_list(request):
    entries = PasswordEntry.objects.filter(user=request.user)
    return render(request, 'password_list.html', {'entries': entries})

@login_required
def add_password(request):
    if request.method == 'POST':
        form = PasswordFormSerializer(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.set_password(form.cleaned_data['password'])
            entry.save()
            return redirect('password_list')
    else:
        form = PasswordFormSerializer()
    return render(request, 'add_password.html', {'form': form})

@login_required
def view_password(request, pk):
    entry = get_object_or_404(PasswordEntry, pk=pk, user=request.user)
    decrypted_password = entry.get_password()
    return render(request, 'view_password.html', {'entry': entry, 'password': decrypted_password})

@login_required
def delete_password(request, pk):
    entry = get_object_or_404(PasswordEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('password_list')
    return render(request, 'delete_password.html', {'entry': entry})

@login_required
def profile(request):
    user = get_object_or_404(User, username=request.user)
    unwanted_keys = ['password', 'id', 'is_staff', 'is_active', 'is_superuser']
    user_details = {key: value for key, value in user.__dict__.items() 
                    if key not in unwanted_keys and not key.startswith('_')}
    return render(request, 'profile.html', {'user_details': user_details})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('password_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def auth_logout(request):
    logout(request)
    return redirect('login') 