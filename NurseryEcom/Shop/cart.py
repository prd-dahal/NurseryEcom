from django.conf import settings
from Shop.models import Product 

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_KEY)
        if not cart:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart
    
    #add in cart
    def add(self, product, quantity):
        product_id = str(product.id)
        if not product_id in self.cart:
            self.cart [product_id] = {'quantity':quantity, 'price':str(product.price)}
        else:
            self.cart [product_id]['quantity'] = int(self.cart [product_id]['quantity'])
            self.cart [product_id]['quantity'] += int(quantity)   
        self.save()
    
    #update cart
    def update(self, product_id, updatedQuantity):
        self.cart[product_id]['quantity'] = updatedQuantity
        self.save()
    
    #delete cart item
    def delete(self, product_id):
        del self.cart[product_id]
        self.save()
    #save
    def save(self):
        self.session.modified = True    
    
    #give list of cart items
    def list(self):
        productData = []
        for productId in self.cart:
            product_temp = {}
            product = Product.objects.get(id=productId)
            product_temp["id"] = productId
            product_temp["product_name"] = product.product_name
            product_temp["quantity"] = self.cart[productId]['quantity']
            product_temp["price"] = self.cart[productId]["price"]
            product_temp["image"] = product.image.url
            product_temp["total"] = int(self.cart[productId]["price"]) * int(self.cart[productId]['quantity'])
            productData.append(product_temp)
        return productData

    
    #gives total price
    def totalPrice(self):
        totalPrice = 0
        for product in self.cart.values():
            totalPrice += (int(product["quantity"] ) * int(product["price"]))
        return totalPrice
      
