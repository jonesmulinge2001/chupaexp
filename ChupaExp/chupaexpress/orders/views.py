from django.shortcuts import render

# Create your views here.
from django.db import transaction
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cart.models import Cart
from .models import Order, OrderItem
from .serializers import OrderItemSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    serializer = OrderItemSerializer(deta=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return Response({'detail': 'Cart is empty.'}, status=400)
    
    items = cart.items.select_related('product').all()
    if not items.exists():
        return Response({'detail': 'Cart is empty.'}, status=400)
    
    with transaction.atomic():
        order = serializer.save(user=request.user)
        for item in items:
            if item.qauntity > item.product.stock:
                return Response({'detail': 'Not enough stock'}, status=400)
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity,
            )
            item.product.save()
    
    return Response(OrderItemSerializer(order).data, status=status.HTTP_201_CREATED)

class OrderListView(generics.ListAPIView):
    pass

class OrderDetailView(generics.RetrieveAPIView):
    pass