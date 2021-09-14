from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps

Art = apps.get_model("art", "Art")

# Create your views here.
def home(request):
    return HttpResponse("<h1> Test home page <\h1>")


from django.views import generic


class HomeView(generic.ListView):
    template_name = "home/home.html"
    context_object_name = "all_art"

    def get_queryset(self):
        return Art.objects.all().order_by("?")


class Shop(generic.ListView):
    template_name = "home/shop.html"
    context_object_name = "all_art"

    def get_queryset(self):
        return Art.objects.all()


class Aboutus(generic.ListView):
    template_name = "home/aboutus.html"
    context_object_name = "all_art"

    def get_queryset(self):
        return Art.objects.all()


def error_404(request, exception):
    return render(request, "home/404.html", locals())
