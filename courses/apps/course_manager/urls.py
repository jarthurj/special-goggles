from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('add_course/', views.add_course, name="add"),
    path('destroy/<int:uid>/',views.destroy, name="destroy")
]
