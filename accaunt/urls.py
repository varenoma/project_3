from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import create_accaunt, accaunt_logout, login_view

app_name = 'accaunt'

urlpatterns = [
    path('create_accaunt', create_accaunt, name='create_accaunt'),
    path('logout', accaunt_logout, name='logout'),
    path('login/', login_view, name='login'),
]