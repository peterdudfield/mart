from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # home
    path("", views.HomeView.as_view(), name="home"),
    path("shop", views.Shop.as_view(), name="shop"),
    path("aboutus", views.Aboutus.as_view(), name="aboutus"),
    path('"https://www.mathsontoast.org.uk"', views.Aboutus.as_view(), name="mathsontoast"),
]
