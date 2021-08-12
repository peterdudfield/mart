from django.views import generic
from .models import Art


class IndexView(generic.ListView):
    template_name = 'art/index.html'
    context_object_name = 'all_art'

    def get_queryset(self):
        print('here')
        return Art.objects.all()


# class DetailView(generic.DetailView):
#     template_name = 'art/detail.html'
#     model = Art
#
#     def get_queryset(self):
#         return Art.objects.all()