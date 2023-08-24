from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='login'),
    path('register/',views.process_reg, name='register'),
    path('login_user/', views.process_log, name='login_user'),
    path('wall/', views.wall, name='wall'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('del_comment/', views.del_comment, name='del_comment'),
]
