from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
from .forms import ProductForm
from users.models import CustomUser


# Create your views here.
def getProducts(req):
    products = Product.objects.all()
    return render(req, "home.html", {"products": products})

def getProduct(req, pid):
    product = get_object_or_404(Product, pk=pid)
    return render(req, "product-detail.html", {"product": product})

def createProduct(req):
    productform = ProductForm()
    if req.method == 'POST':
        try:
            owner = CustomUser.objects.get(id=req.user.id)
            Product.objects.create(title = req.POST["title"], description = req.POST["description"], price = req.POST["price"], stock = req.POST["stock"], category = req.POST["category"], owner = owner) 
            return render(req, "product-create.html", {"form": productform, "message": 'Product created successfully'})
        except Exception as error:
            return render(req, "product-create.html", {"form": productform, "error": error})
    else:
        return render(req, "product-create.html", {"form": productform})

def updateProduct(req, pid):
    if req.method == 'POST':
        try:
            product = get_object_or_404(Product, pk=pid)
            productform = ProductForm(req.POST, instance=product)
            productform.save()
            return redirect('product-detail', pid=pid)
        except Exception as error:
            return render(req, "product-update.html", {"form": productform, "product": product, "error": error})
            
    product = get_object_or_404(Product, pk=pid)    
    productform = ProductForm(instance=product)
    return render(req, "product-update.html", {"form": productform, "product": product})

def deleteProduct(req, pid):
    product = get_object_or_404(Product, pk=pid)
    try:
        product.delete()
        return redirect('home')
    except Exception as error:
        productform = ProductForm(instance=product)
        return render(req, "product-update.html", {"form": productform, "product": product, "error": error})

def buyProduct(req, pid):
    product = get_object_or_404(Product, pk=pid)
    return render(req, "product-buy.html", {"product": product})
