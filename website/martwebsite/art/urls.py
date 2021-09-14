from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # art
    path("", views.IndexView.as_view(), name="art/index"),
    # path('<str:pk>', views.DetailView.as_view(), name='detail'),
    # art/9
    # path('<str:pk>', views.IndexView.as_view(), name='detail'),
]
