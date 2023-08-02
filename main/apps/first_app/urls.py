from django.urls import re_path, path
from . import views           # This line is new!
urlpatterns = [
  path("", views.index),     # This line has changed!
  path("butt", views.butt)
]

