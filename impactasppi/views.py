from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"


class LoginPageView(TemplateView):
    template_name = "login.html"
