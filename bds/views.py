from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from .models import Product


class Home(ListView):
    model = Product
    template_name = 'base.html'
    context_object_name = 'products'