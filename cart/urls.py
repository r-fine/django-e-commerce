from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>',
         views.remove_from_cart, name='remove_from_cart'),
    path('remove_item/<int:product_id>', views.remove_item, name='remove_item'),

]
