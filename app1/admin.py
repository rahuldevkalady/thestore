from django.contrib import admin
from .models import*
from .forms import *
# Register your models here.

admin.site.register(supplier)
admin.site.register(category)
admin.site.register(product_s)
admin.site.register(order)
admin.site.register(order_item)
admin.site.register(customer)
admin.site.register(thestore_admin)
admin.site.register(Message)
admin.site.register(cart)
admin.site.register(cart_item)
