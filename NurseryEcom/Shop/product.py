from .models import Product

class productClass:
    def __init__(self):
        self.products = []
    def loopProduct(self, object):
        for product in object:
            temp_product = {}
            temp_product['id'] = product.id
            temp_product['product_name'] = product.product_name
            temp_product['price'] = product.price
            temp_product['category'] = product.category
            temp_product['description'] = product.description
            temp_product['image'] = product.image.url
            self.products.append(temp_product)
    
    def getProduct(self):
        self.loopProduct(Product.objects.all())
        return self.products
    
    def filterProduct(self, filterData):
        self.loopProduct(Product.objects.filter(category=filterData))
        return self.products
    
    def searchProduct(self, keyword):
        self.loopProduct(Product.objects.filter(product_name__contains=keyword))
        return self.products
    