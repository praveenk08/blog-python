from django.shortcuts import render, HttpResponse
from home.models import Contact, product
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home/index.html')
    # return HttpResponse('heml my home page')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['mail']
        content = request.POST['comment']
        if len(name)<2 or len(phone)<10 or len(email)<4 or len(content)<5:
            messages.error(request,' Something went wrong')
        else:
            contact = Contact(name=name, phone=phone, email=email, content=content)
            messages.success(request,'submit successfully')
            contact.save()
    return render(request, 'home/contacts-2.html')
    # return HttpResponse('heml my contact page')
def about(request):
    return render(request, 'home/about-us.html')
    # return HttpResponse('heml my about page')
def product(request):
    allproduct = product.objects.all()
    print(allproduct)
    context = {'allproduct' : allproduct}
    return render(request, 'shop/shop_sidebar_single=left.html',context)

def productDetail(request):
    return render(request, 'shop/shop_sidebar_single=left.html')

def shop(request):
    allproduct = product.objects.all()
    print(allproduct)
    context = {'allproduct' : allproduct}
    return render(request,'shop/shop_layout=left.html',context)

def cart(request):
    return render(request, 'shop/shop_sidebar_single.html')

