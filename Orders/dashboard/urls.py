from django.urls import path 
from .views import * 


urlpatterns = [
    path('home',HomeView.as_view(),name='home'),
    path('product',ProductView.as_view(),name='products'),
    path('orders', OrdersView.as_view(), name='orders')
]