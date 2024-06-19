from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
    context = {}
    return render(request, 'tuestilo/base.html', context)

def info(request):
    context = {}
    return render(request, 'tuestilo/info.html', context)

def catalogo(request):
    context = {}
    return render(request, 'tuestilo/catalogo.html', context)

def contacto(request):
    context = {}
    return render(request, 'tuestilo/contacto.html', context)

@login_required

def carro(request):
    context = {}
    return render(request, 'tuestilo/carro.html', context)