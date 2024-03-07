from django.contrib import admin
from typing import Final
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials


# PASSO 2: CARREGAR O DISCORD TOKEN DE UM LUGAR SEGURO
load_dotenv()
KEY: Final[str] = os.getenv('KEY')



cred = credentials.Certificate(KEY)
firebase_admin.initialize_app(cred)


# Register your models here.
