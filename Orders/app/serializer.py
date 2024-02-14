from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Product
        fields = ['id', 'name', 'price', 'quantity', 'created_at']

class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model= Order
        fields = ['id', 'order_items', 'products', 'amount', 'created_at']
