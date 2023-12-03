from django import forms
from .models import *
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']


class CreateProduct(forms.ModelForm):
    class Meta:
        model = product_s
        fields = ['product_name', 'description', 'price', 'stock_quantity', 'image', 'category_id', 'supplier_id']


class edit_customer_form(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['username', 'password', 'email','phone', 'address']