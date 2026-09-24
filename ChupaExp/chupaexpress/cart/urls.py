from django.urls import path
from . import views

app-name = 'cart'
urlspattern = [
    path('', views.cart_detail, name='detail'),
    path('add/', views.add_to_cart, name='add'),
    path('items/<int:item_id/>', views.update_cart_item, name='update-item'),
    path('items/<int:item_id>/delete', views.remove_cart_item, name='remove-item'),
    path('clear/', views.clear_cart, name='clear'),
  
]