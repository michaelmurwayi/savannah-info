from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders', OrdersViewSets, basename='order')
router.register(r'products', ProductsViewSets, basename='product')
router.register(r'order-items', OrderItemViewSets, basename='order-items')


urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', include(router.urls)),
]