from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
import logging
import pyrebase

log = logging

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
database = firebase.database()

# Create your views here.


def login(request):
    return render(request, "login.html")


def home(request):
    return render(request, "home.html")


def postLogin(request):
    email = request.POST.get('lemail')
    pasw = request.POST.get('lpass')
    try:
        user = auth.sign_in_with_email_and_password(email, pasw)
    except user.DoesNotExist:
        message = "Invalid Credentials!!Please ChecK your Data"
        return render(request, "login.html", {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return redirect('/', {"email": email})


def postSignUp(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    name = request.POST.get('name')
    print(name)
    try:
        user = auth.create_user_with_email_and_password(email, pasw)
    except:
        message = "Dados incorretos/Já Cadastrados!"
        return redirect('/login', {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return redirect("/login", {"email": email})


def logout(request):
    uid = request.session['uid']
    try:
        del request.session['uid']
    except uid.DoesNotExist:
        pass
    return render(request, "login.html")


def forget(request):
    if request.method == 'GET':
        return render(request, "forget.html")
    
    if request.method == "POST":
        email = request.POST.get('remail')
        try:
            auth.send_password_reset_email(email)
            message  = "Email para troca de senha enviado com sucesso!"
            return redirect("/login", {"msg":message})
        except:
            message  = "Algo deu errado! Cheque se esse é o seu email de cadastro!"
            return redirect("/forget", {"msg":message})
