from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
import logging
import pyrebase
import sweetify


log = logging

config = {'apiKey': "AIzaSyDTm56zPBOzgblJgsnUHD-qXI7-vXJVfk4",
  'authDomain': "impacta--sppi.firebaseapp.com",
  'databaseURL': "https://impacta--sppi-default-rtdb.firebaseio.com",
  'projectId': "impacta--sppi",
  'storageBucket': "impacta--sppi.appspot.com",
  'messagingSenderId': "700556689434",
  'appId': "1:700556689434:web:b5347313e1273b19fa91a3",
  'measurementId': "G-W9XPPBZG1S"}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

# Create your views here.


def home(request):
    if request.method == "GET":
        try:
            user_id = request.session['localID']
            if user_id in locals():
                return render(request, "home.html", {"uid": user_id})

            else:
                return render(request, "home.html")
        except Exception as xptc:
            return render(request, "home.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        email = request.POST.get('lemail')
        pasw = request.POST.get('lpass')
        try:
            user = auth.sign_in_with_email_and_password(email, pasw)
        except Exception as xecpt:
            print(xecpt)
            sweetify.warning(request, "Erro! Verifique suas credenciais")
            return render(request, "login.html")
        session_id = user['idToken']
        user_id = user['localId']
        request.session['localID'] = str(user_id)
        request.session['uid'] = str(session_id)
        sweetify.success(request, "Login realizado com!")
        return redirect('/', {"sid": str(user_id)})


def register(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    name = request.POST.get('name')
    print(name)
    try:
        user = auth.create_user_with_email_and_password(email, pasw)
    except Exception as xecpt:
        print(xecpt)
        sweetify.warning(request, "Dados incorretos/Ja Cadastrados.")
        return redirect('/login', message="TESTE")
    session_id = user['idToken']
    user_id = user['localId']
    db.child(str(user_id)).set(name)
    request.session['uid'] = str(session_id)
    sweetify.success(request, "Cadastro efetuado com sucesso!")
    return redirect("/login", {"email": email})


def logout(request):
    uid = request.session['uid']
    try:
        del request.session['uid']
    except uid.DoesNotExist:
        pass
    sweetify.success(request, "Logout efetuado com sucesso!")
    return redirect("/login")


def forget(request):
    if request.method == 'GET':
        return render(request, "forget.html")

    if request.method == "POST":
        email = request.POST.get('remail')
        try:
            auth.send_password_reset_email(email)
            sweetify.success(request, "Solicitação Enviado!")
            return redirect("/login")
        except Exception as xecpt:
            print(xecpt)
            sweetify.warning(request, "Email não cadastrado!")
            return redirect("/forget")
