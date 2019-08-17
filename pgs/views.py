from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Pgs


class PgsListView(ListView):
    model = Pgs
    template_name = 'home.html'


class PgsDetailView(DetailView):
    model = Pgs
    template_name = 'pg_detail.html'


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
