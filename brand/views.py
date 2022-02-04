from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def show_list(request):
    brands = Brand.objects.all()   
    return render(request, "brand/list.html", {"brands":brands})

def show_detail(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    return render(request, "brand/detail.html", {"brand":brand})

def wish_brand(request):
    pass