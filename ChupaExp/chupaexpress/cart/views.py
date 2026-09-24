from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

def get_or_create_cart(user):
    cart,_ = Cart.objects.get_or_create(user=user)
    return cart

@api_view(['GET'])
@permission_classes(['IsAuthendicated'])
def cart_detail(request):
    cart = get_or_create_cart(request.user)
    return Response(CartSerializer(cart).data)

@api_view(['POST'])
@permission_classes(['IsAuthendicated'])
def add_to_cart(request):
    cart = get_or_create_cart(request.user)
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    Product = get_object_or_404(Product, id=product_id, available=True)
    if quantity < 1:
        return Response({'detail': 'Quantity must be greater than 1'}, status=400)
    if quantity > Product.stock:
        return Response({'detail': 'Not enough stock'}, status=status.HTTP_400_BAD_REQUEST)
    item, created = CartItem.objects.get_or_create(cart=cart, Product=Product)
    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity
        item.save()
        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)
    

@api_view(['PATCH'])
@permission_classes(['IsAuthendicated'])
def update_cart_item(request, item_id):
    cart = get_or_create_cart(request.user)
    item = get_object_or_404(CartItem, id = item_id, cart=cart)
    quantity = int(request.data.get('quantity', item.quantity))
    if quantity < 1:
        return Response({'detail': 'Quantity must be greater than 1'}, status=400)
    if quantity > Product.stock:
        return Response({'detail': 'Not enough stock'}, status=status.HTTP_400_BAD_REQUEST)
    
    item.quantity = quantity
    item.save()
    return Response(CartItemSerializer(cart).data)

# delete individual item
@api_view(['DELETE'])
@permission_classes(['IsAuthendicated'])
def remove_cart_item(request, item_id):
    cart = get_or_create_cart(request.user)
    item = get_object_or_404(CartItem, id = item_id, cart=cart)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# clear cart / empty cart
@api_view(['DELETE'])
@permission_classes(['IsAuthendicated'])
def clear_cart(request):
    cart = get_or_create_cart(request.user)
    cart.items.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)