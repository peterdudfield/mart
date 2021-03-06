from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path("email/", views.emailView, name="email"),
    path("success/", views.successView, name="success"),
]
