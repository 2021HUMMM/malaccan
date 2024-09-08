from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Item

def show_main(request):
    products = Item.objects.all()  # Mengambil semua produk dari database
    context = {
        'shop_name': 'Malaccan',
        'npm' : '2306210714',
        'name' : 'Ilham Satya Nusabhakti',
        'class' : 'PBP C',
        'products': products,  # Produk-produk yang diambil dari model
    }
    return render(request, "main.html", context)
