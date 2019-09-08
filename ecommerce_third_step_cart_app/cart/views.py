from django.shortcuts import render
from shop.models import Products
from .models import Cart , CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# Three tasks to perform in this application
# No-01. If session ID is created on the users browser
# No-02. - Add product on the shopping cart 
# No-03. - Display items on the shopping cart

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.creata()
    return cart

def add_cart(request,product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExists:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExists:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request,total=0,counter=0,cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request,'cart.html',dict=(cart_items = cart_items , total= total ,counter=counter))