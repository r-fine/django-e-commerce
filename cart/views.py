from django.http.response import HttpResponseRedirect
from store.models import Product
from django.shortcuts import render
from django.contrib import messages

from .models import Cart, CartItem


def cart_detail(request):
    try:
        cart_items, quantity, total_quantity, total, delivery_charge, grand_total = None, 0, 0, 0, 0, 0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        total_quantity = quantity
        delivery_charge = 60
        grand_total = total + delivery_charge
    except Cart.DoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'total_quantity': total_quantity,
        'cart_items': cart_items,
        'delivery_charge': delivery_charge,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart/cart_detail.html', context)


def _cart_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, product_id):
    product = Product.products.get(id=product_id)
    cart = Cart.objects.get_or_create(cart_id=_cart_id(request))[0]
    cart.save()

    try:
        cart_item = CartItem.objects.get(
            cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            cart=cart, product=product, quantity=1)
        cart_item.save()
    # return HttpResponse(cart_item.product)
    messages.warning(request, 'Successfully added to cart')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, product_id):
    product = Product.products.get(id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_item(request, product_id):
    product = Product.products.get(id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
