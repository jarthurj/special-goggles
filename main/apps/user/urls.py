from django.urls import re_path, path

from . import views           # This line is new!
urlpatterns = [
  path("", views.index, name="index"),     # This line has changed!
  path("register/", views.register),
  path("login/", views.login),
  path("users/new/", views.new),
  path("users/", views.users)
]
