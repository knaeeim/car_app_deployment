from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('registration/', RegistartionView.as_view(), name='registartion'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('edit_profile/', UserEditProfile.as_view(), name='edit_profile'),
    path('change_password/', PasswordChangeView.as_view(), name='password_change'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', user_logout, name='logout'),
]