from django.shortcuts import render,redirect
from .models import Product
from .cart import Cart
from .product import productClass
# Create your views here.

def index(request):
    cart = Cart(request)
    totalPrice = cart.totalPrice()
    product = productClass()
    products = product.getProduct()
    return render(request, 'Shop/shop.html',{"products": products,"totalPrice":totalPrice,'fromIndex':True})

def filter(request, category):
    cart = Cart(request)
    totalPrice = cart.totalPrice()
    product = productClass()
    products = product.filterProduct(category)
    return render(request, 'Shop/shop.html',{"products": products,"totalPrice":totalPrice,'fromIndex':False})

def search(request):
    if request.method == "POST":
        productKeyword = request.POST['keyword']
        cart = Cart(request)
        totalPrice = cart.totalPrice()
        product = productClass()
        products = product.searchProduct(productKeyword)
        return render(request, 'Shop/shop.html',{"products": products,"totalPrice":totalPrice,'fromIndex':False})


def add_to_cart(request, id):
    if request.method == 'POST':
        if request.POST['fromIndex']:
            print("From Index")
        else:
            print("Not from Index")
        product = Product.objects.get(id=id)
        cart = Cart(request)
        quantity = request.POST['quantity']
        if not quantity:
            quantity = 1
        cart.add(product, quantity)
        print(product.category)
        
        if request.POST['fromIndex'] == 'True/':
            print("From the index")
            return redirect("Shop:shopIndex")
        else:
            print("Not from the index")
            return redirect("Shop:filter", category=product.category)
        
    
def display_cart(request):
    cart = Cart(request)
    cartProducts = cart.list()
    totalPrice = cart.totalPrice()
    return render(request,'Shop/cartDisplay.html',{"cartProducts":cartProducts, "totalPrice":totalPrice})

def update_cart(request):
    if request.method == "POST":
        quantity = request.POST["updateQuantity"]
        id = request.POST["id"]
        cart = Cart(request)
        cart.update(id, quantity)
        return redirect("Shop:display_cart")
def delete_cart(request):
   if(request.method == "POST"):
       id = request.POST['id']
       cart = Cart(request)
       cart.delete(id)
       return redirect("Shop:display_cart")

        