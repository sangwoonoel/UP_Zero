from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def show_list(request):
    brands = Brand.objects.all()   
    return render(request, "brand/list.html", {"brands":brands})

def show_detail(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    wish_cnt = BrandLike.objects.filter(brand=brand).count()
    return render(request, "brand/detail.html", {"brand":brand, "wish_cnt":wish_cnt})

def wish_brand(request):
    pass