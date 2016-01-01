from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from fridgeroom.models import StandartPublication

class PubsList(ListView):
    model = StandartPublication
    template_name="fridgeroom/pub_list.html"
    ordering = "-datetime"
    
class PubDetail(DetailView):
    model = StandartPublication
    template_name="fridgeroom/pub_detail.html"