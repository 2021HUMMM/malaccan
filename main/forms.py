from django.forms import ModelForm
from main.models import Product
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "stock", "price", "description", "image"]
    
    image = forms.ImageField(required=True, label='Product Image', help_text='Upload an image of the product.')