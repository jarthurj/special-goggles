from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('success/', views.success, name="success")
]
