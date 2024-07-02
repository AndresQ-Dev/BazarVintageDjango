from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'banner_image': 'img/banner_home.jpg', 
        'banner_text': 'Vintage & Deco',})

def products(request):
    return render(request, 'products.html', {'banner_image': 'img/banner_products.jpg', 'banner_text': 'Nuestros productos'})

def sales(request):
    return render(request, 'sales.html', {'banner_image': 'img/banner_sale.jpeg', 'banner_text': ''})

def about(request):
    return render(request, 'about.html', {'banner_image': 'img/banner_about.jpg', 'banner_text': 'Sobre nosotros'})

def contact(request):
    return render(request, 'contact.html', {'banner_image': 'img/banner_contact.jpg', 'banner_text': 'Contacto'})