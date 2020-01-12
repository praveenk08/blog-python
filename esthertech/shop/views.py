from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.
def shop(request):
    return render(request,'shop/shop_layout=left.html')

def cart(request):
	return render(request, 'home/about-us.html')

def productDetail(request):
    return render(request, 'shop/shop_sidebar_single=left.html')

def product(request):
    return render(request, 'home/about-us.html')

 