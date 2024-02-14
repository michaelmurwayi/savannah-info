from django.shortcuts import render
from rest_framework import generics, viewsets
from django.views.generic.edit import CreateView
from .models import *
from .serializer import *

# Create your views here.

class ProductsViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrdersViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSets(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer