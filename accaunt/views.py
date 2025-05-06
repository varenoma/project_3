from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

# Create your views here.


def create_accaunt(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('app:index'))
    else:
        form = UserCreationForm()

    return render(request, 'accaunt/create_accaunt.html', {'form': form})


def accaunt_logout(request):
    logout(request)
    return redirect('app:index')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app:index')
    else:
        form = AuthenticationForm()

    return render(request, 'accaunt/login.html', {'form': form})