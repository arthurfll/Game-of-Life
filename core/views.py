from django.shortcuts import render
from loja.models import *



def home(request):
    products = Product.objects.all()[0:6]
    return render(request,'core/home.html',{'products':products})


def carrinho(request):
    return render(request,"core/carrinho.html")