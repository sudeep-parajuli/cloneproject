       
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts import forms

class SignUp(CreateView):
    form_class = forms.userRegisterForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"