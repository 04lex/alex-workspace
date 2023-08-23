from django.shortcuts import render, redirect
from .cart import Cart
# Create your views here.
from store.models import Product

def cart_view(request):
  
    current_cart = Cart(request)
    nr_produse = len(current_cart)

    products_dict = current_cart.products
    products =  Product.objects.filter(pk__in=products_dict.keys())

    print(nr_produse)
    context = {'nr_produse':nr_produse,
    'products':products}
    return render(request, 'cart.html', context)


def clear_cart_view(request):
    current_cart = Cart(request)
    current_cart.clear_cart()
    return redirect('cart:cart_details')


def add_product_to_cart_view(request):
    current_cart = Cart(request)
    current_cart.add_product(1, 1)
    return redirect('cart:cart_details')

