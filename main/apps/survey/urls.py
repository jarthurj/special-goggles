from django.urls import re_path, path
from . import views           # This line is new!
urlpatterns = [
  path("", views.index, name="index"),     # This line has changed!
  path("surveys/", views.surveys),
  path("surveys/new", views.new)
]

    # /surveys - display "placeholder to display all the surveys created"
    # /surveys/new - display "placeholder for users to add a new survey
