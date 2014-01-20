from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
# Create your views here.
from classified.models import Classified


class ClassifiedListView(ListView):
    model = Classified


class ClassifiedDetailView(DetailView):
    model = Classified
