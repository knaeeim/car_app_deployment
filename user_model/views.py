from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, FormView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
class RegistartionView(CreateView):
    model = User
    form_class = RegistartionForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Registration successful')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Registration'
        return context
    
class UserLoginView(LoginView):
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Login Credentials are incorrect')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Login"
        return context

@method_decorator(login_required, name='dispatch')
class UserEditProfile(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'registration.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully')
        return super().form_valid(form)
    
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Edit Profile"
        return context
    
# class UserPasswordChange(FormView):
@method_decorator(login_required, name="dispatch")
class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'registration.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully')
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwarg = super().get_form_kwargs()
        kwarg['user'] = self.request.user
        return kwarg
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Change Password"
        return context

@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('login')