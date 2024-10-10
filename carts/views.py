from django.shortcuts import render, redirect
from users.models import CustomUser
from products.models import Product
from .models import Cart


# Create your views here.
def getCart(req, uid):
    cart = Cart.objects.filter(userId=uid)
    for prod in cart:
        prod.subtotal = prod.productId.price * prod.quantity

    total = 0
    for subTotal in cart:
        total = total + subTotal.subtotal
    return render(req, "cart-detail.html", {"cart": cart, "total": total})

def emptyCart(req, uid):
    try:
        cart = Cart.objects.filter(userId=uid).delete()
        if cart[0] != 0:
            updatedCart = Cart.objects.filter(userId=uid)
            return render(req, "cart-detail.html", {"cart": updatedCart, "message": 'Cart is now empty.'})
    except Exception as error:
        updatedCart = Cart.objects.filter(userId=uid)
        return render(req, "cart-detail.html", {"cart": updatedCart, "error": error})

def deleteProductCart(req, uid, pid):
    try:
        user = CustomUser.objects.get(id=uid)
        product = Product.objects.get(id=pid)
        cart = Cart.objects.get(userId=user, productId=product).delete()
        if cart[0] != 0:
            updatedCart = Cart.objects.filter(userId=uid)
            return render(req, "cart-detail.html", {"cart": updatedCart, "message": f'The product ID: {pid} was successfully removed.'})
    except Exception as error:
        cart = Cart.objects.filter(userId=uid)
        for prod in cart:
            prod.subtotal = prod.productId.price * prod.quantity

        total = 0
        for subTotal in cart:
            total = total + subTotal.subtotal
        return render(req, "cart-detail.html", {"cart": cart, "error": error, "total": total})

def buyCart(req, uid):
    cart = Cart.objects.get(userId=uid)
    return render(req, "cart-detail.html", {"cart": cart, "message": 'Coming soon.'})

def addToCart(req, uid, pid):
    if req.method == 'POST':
        try:
            user = CustomUser.objects.get(pk=uid)
            product = Product.objects.get(pk=pid)
            newProductToCart = Cart(id=None, userId=user, productId=product, quantity=req.POST["quantity"])
            newProductToCart.save()
            redirect('home')
        except Exception as error:
            products = Product.objects.all()
            return render(req, "home.html", {"products": products, "error": error})
        
    cart = Cart.objects.filter(userId=uid)
    return render(req, "cart-detail.html", {"cart": cart})
