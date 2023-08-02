from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
	path("", views.index, name="index"),
	path("randw/", views.randw, name="randw"),
	path("reset/", views.index, name="reset"),
	path('admin/', admin.site.urls),
]