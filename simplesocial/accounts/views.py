from django.contrib.auth import forms
from django.shortcuts import render
# importing generic views
from django.views.generic import (CreateView)
# for redirecting once us loggedin or loggedout
from django.urls import reverse_lazy
# importing forms
from . import forms

# Create your views here.

# new user signing up 
class SignUp(CreateView):
    # connecting to te form
    form_class = forms.UserCreateForm
    # redirecting to login page after signup
    success_url = reverse_lazy('login')
    # connecting to template 
    template_name = 'accounts/signup.html'