
"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views
urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('admin/', views.admin, name="admin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('show/<int:uid>', views.show, name="show"),
    path('edit/', views.edit, name="edit"),
    path('admin_edit/', views.admin_edit, name="admin_edit"),
    path('register_user/', views.register_user, name="register_user"),
    path('login_user/', views.login_user, name="login_user"),
    path('add_post/', views.add_post, name="add_post"),
    path('add_comment/', views.add_comment, name="add_comment"),
    path('edit_pw/', views.edit_pw, name="edit_pw"),
    path('edit_user/', views.edit_user, name="edit_user")


]
