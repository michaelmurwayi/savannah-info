from django.shortcuts import render
from rest_framework import generics
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    # Your home page logic here
    return render(request, 'home.html')