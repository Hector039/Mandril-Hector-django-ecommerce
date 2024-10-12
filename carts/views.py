from django.shortcuts import render, redirect
from users.models import CustomUser
from products.models import Product
from products.forms import ProductSearchForm
from .models import Cart

def getUserCart(req, uid, msg='', err=''):
    try:
        cart = Cart.objects.filter(userId=uid)
        for prod in cart:
            prod.subtotal = prod.productId.price * prod.quantity

        total = 0
        for subTotal in cart:
            total = total + subTotal.subtotal

        return render(req, "cart-detail.html", {"cart": cart, "total": total, "message": msg})
    except Exception:
        return render(req, "cart-detail.html", {"cart": cart, "total": total, "error": err})
    
    

# Create your views here.
def getCart(req, uid):
    return getUserCart(req, uid)

def emptyCart(req, uid):
    try:
        cart = Cart.objects.filter(userId=uid).delete()
        if cart[0] != 0:
            return getUserCart(req, uid, msg='Cart is now empty.')
    except Exception as error:
        return getUserCart(req, uid, err=error)

def deleteProductCart(req, uid, pid):
    try:
        user = CustomUser.objects.get(id=uid)
        product = Product.objects.get(id=pid)
        cart = Cart.objects.get(userId=user, productId=product).delete()
        if cart[0] != 0:
            return getUserCart(req, uid, msg=f'The product ID: {pid} was successfully removed.')
    except Exception as error:
        return getUserCart(req, uid, err=error)

def buyCart(req, uid):
    return getUserCart(req, uid, msg='Coming soon.')

def addToCart(req, uid, pid):
    searchForm = ProductSearchForm(req.GET)
    if req.method == 'POST':
        try:
            user = CustomUser.objects.get(pk=uid)
            product = Product.objects.get(pk=pid)
            newProductToCart = Cart(id=None, userId=user, productId=product, quantity=req.POST["quantity"])
            newProductToCart.save()
            redirect('home')
        except Exception as error:
            products = Product.objects.all()
            return render(req, "home.html", {"products": products, "error": error, 'searchForm': searchForm})
        
    return getUserCart(req, uid)
