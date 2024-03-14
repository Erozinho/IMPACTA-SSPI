from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from django.contrib import messages
import pyrebase

config = {'apiKey': "AIzaSyDTm56zPBOzgblJgsnUHD-qXI7-vXJVfk4",
  'authDomain': "impacta--sppi.firebaseapp.com",
  'projectId': "impacta--sppi",
  'storageBucket': "impacta--sppi.appspot.com",
  'messagingSenderId': "700556689434",
  'appId': "1:700556689434:web:b5347313e1273b19fa91a3",
  'measurementId': "G-W9XPPBZG1S",
  'databaseURL' : ''}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database() #comando necessário pra usar um banco de dados do firebase

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"


class LoginPageView(TemplateView):
    template_name = "login.html"
    redirect_authenticated_user = True
    
    def form_invalid(self, form):
        messages.error(self.request,'E-mail ou senha inválidos!')
        return self.render_to_response(self.get_context_data(form=form))
