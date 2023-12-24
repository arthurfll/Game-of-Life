from django.shortcuts import render

def home(request):
    return render(request,'core/home.html')

def sobre(request):
    return render(request,'core/sobre.html')

def carrinho(request):
    return render(request,"core/carrinho.html")