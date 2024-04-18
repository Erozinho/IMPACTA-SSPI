from django.shortcuts import render
from django.shortcuts import redirect
import logging
import pyrebase
import sweetify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
# from django.db import models


# class Propiedade(models.Model):
#     nome = models.CharField(max_length=100)
#     tipo = models.CharField(max_length=25)
#     valor = models.DecimalField()
#     img = models.CharField(max_length=400)
#     desc = models.CharField(max_length=300)

#     @classmethod
#     def create(cls, title, tipo, valor, img, desc):
#         propiedade = cls(title=title,
#                          tipo=tipo,
#                          valor=valor,
#                          img=img,
#                          desc=desc)
#         # do something with the book
#         return propiedade


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

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


clientid = "ede3ed94c337f67"

# file = request.files['file']
# file.save((os.path.join(dir_root, secure_filename(file.filename))))
# file = os.path.join(dir_root, secure_filename(file.filename))

# print('printado',nome)

# # upando img e apagando temp
# im = pyimgur.Imgur(clientid)
# upimg = im.upload_image(file)
# os.remove(file)
# db.collection("users").document(session['cpf']).update({"pfp": upimg.link})


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
            print(xptc)
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
        print(f"{user} criado com sucesso.")
    except Exception as xecpt:
        print(xecpt)
        sweetify.warning(request, "Dados incorretos/Ja Cadastrados.")
        return redirect('/login')
    db.collection("usuarios").document(str(email)).set({"Nome": str(name), "email": str(email)})
    sweetify.success(request, "Cadastro efetuado com sucesso!")
    return redirect("/login")


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


def terrenos(request):
    if request.method == 'GET':
        propiedades = {}
        docs = db.collection("produtos").stream()
        for doc in docs:
            propiedades[doc.id] = doc.to_dict()

        context = {'propiedades': propiedades}
        return render(request, "terrenos.html", context)


def product_detail(request, nome):
    if request.method == 'GET':
        rancho = {}
        docs = (db.collection("produtos").
                where(filter=FieldFilter("nome", "==", nome)).stream())

        for doc in docs:
            rancho[doc.id] = doc.to_dict()

        context = {'propiedades': rancho}
        return render(request, 'terreno.html', context)
