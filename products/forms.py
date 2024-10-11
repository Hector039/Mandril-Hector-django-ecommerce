from django.forms import ModelForm
from django import forms
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'stock', 'category', 'status']

class ProductSearchForm(forms.Form):
    category = (
        ('all', 'All'),
        ('electronics', 'Electronics'),
        ('furniture', 'Furniture'),
        ('accesories', 'Accesories'),
        ('computing', 'Computing'),
        ('other', 'Other'))

    order_by_price = (
        ("all", 'All'),
        ("ascending", 'Ascending'),
        ("descending", 'Descending'))

    title = forms.CharField(max_length=20, required=False)
    category = forms.ChoiceField(choices=category, required=False)
    price = forms.ChoiceField(choices=order_by_price, required=False)