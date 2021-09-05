from django.db import models
from django.contrib.auth.models import User
# Create your models here.
categoryChoice = (
    ('IN', "Indoor"),
    ('OUT', "Outdoor"),
    ('SUC', "Saculent"),
    ('SE', "Seasonal"),
    ('OTH',"Others")
)
status = (
    ('NP', "Not Paid"), 
    ('HP', "Half Paid"),
    ('FP', "Full Paid"),
    ("SHIP", "Shipped")
)
class Product(models.Model):
    product_name = models.CharField( max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length = 3 , choices = categoryChoice)
    description = models.TextField(max_length = 500)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.product_name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    num = models.IntegerField()
    status = models.CharField(max_length = 4, choices = status)

    def __str__(self):
        return self.product.product_name + " ordered by " + self.user.username