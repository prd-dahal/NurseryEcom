from django.contrib import admin

from Shop.models import Product, Order
# Register your models here.
admin.site.register(Order)
admin.site.register(Product)