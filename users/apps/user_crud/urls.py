from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('users/', views.index, name='index'),
    path('users/<int:uid>/', views.user, name='user'),
    path('users/new/', views.users_new, name='new'),
    path('users/create/', views.users_create, name='create'),
    path('users/<int:uid>/edit/', views.users_edit, name='edit'),
    path('users/<int:uid>/destroy/', views.destroy, name='destroy'),
    path('users/<int:uid>/update/',views.update, name='update')
]
