from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.total()
    return render(
        request,
        "cart_summary.html",
        {"cart_products": cart_products, "quantities": quantities, "totals": totals},
    )


def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for Post
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        # save to session
        cart.add(product=product, quantity=product_qty)
        # get cart quantity
        cart_quantity = cart.__len__()

        # return response
        # response = JsonResponse({"Produc Name: ": product.name})
        response = JsonResponse({"qty: ": cart_quantity})
        messages.success(request, "There was  an  adding this item...!")
        return response


def cart_delete(request):
    cart = Cart(request)
    # test for Post
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        # call delete function
        cart.delete(product=product_id)
        response = JsonResponse({"product": product_id})
        messages.success(request, "Iten=m Deleted Form Shopping Cart...!")
        return response
        # return redirect('cart_summary')


def cart_update(request):
    cart = Cart(request)
    # test for Post
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({"qty": product_qty})
        messages.success(request, "Your Cart has been update...!")
        return response
        # return redirect('cart_summary')
