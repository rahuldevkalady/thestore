from django.db import models
from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db import models
# from django import forms
from django.db.models.manager import EmptyManager
from django.utils import timezone
from django.utils.itercompat import is_iterable
from django.utils.translation import gettext_lazy as _

# from .validators import UnicodeUsernameValidator


# Create your models here.

# Login Database Models supplier, customer , admin
class supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    session_token = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gstin = models.CharField(max_length=15)
    shop_name = models.CharField(max_length=15)
    address = models.TextField()
    aadhar = models.CharField(max_length=15)
    def __str__(self):
        return self.username

class customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    def __str__(self):
        return self.username

class thestore_admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username






# the store Database Models

class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class product_s(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image = models.ImageField(blank=True, upload_to='media/')
    category_id = models.ForeignKey(category, on_delete=models.SET_NULL, null=True)
    supplier_id = models.ForeignKey(supplier, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.product_name



# cart
class cart(models.Model):
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(product_s, through='cart_item')
    def __int__(self):
        return self.customer_id


class cart_item(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product_s, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __int__(self):
        return self.cart

# order processing
class order(models.Model):
    user = models.ForeignKey(customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(product_s, through='order_item')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='Pending')


class order_item(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(product_s, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



# Contact
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=100)

    def __int__(self):
        return self.email
