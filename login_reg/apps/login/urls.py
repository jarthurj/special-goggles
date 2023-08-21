from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/',views.index, name="login"),
    path('processreg/', views.process_reg, name="processreg"),
    path('successreg/', views.success_reg, name="successreg"),
    path('processlog/', views.process_log, name="processlog"),
    path('successlog/', views.success_log, name="successlog")
]
