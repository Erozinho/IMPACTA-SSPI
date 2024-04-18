"""
URL configuration for impactasppi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),  # type: ignore
    path("register/", views.register, name="register"),  # type: ignore
    path('logout/', views.logout, name="log"),
    path('forget/', views.forget),  # type: ignore
    path('terrenos/', views.terrenos, name="terrenos"),
    path('<str:nome>/', views.product_detail, name='product_detail'),
]

urlpatterns += staticfiles_urlpatterns()
