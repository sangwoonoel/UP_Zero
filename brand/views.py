from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import *

def show_list(request):
    if request.GET:
        keyword = request.GET.get('keyword')
        brands = Brand.objects.all().filter(name__icontains=keyword)
    else:
        brands = Brand.objects.all()

    return render(request, 'brand/list.html', {'brands': brands})


def show_detail(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    like_cnt = BrandLike.objects.filter(brand=brand).count()

    try: # 로그인 한 상태일 때
        if BrandLike.objects.filter(user=request.user, brand=brand).exists():
            is_liked = True
        else:
            is_liked = False
    
    except TypeError: # 로그인 안 한 상태일 때       
        is_liked = False
        
    return render(request, "brand/detail.html", {"brand":brand, "is_liked":is_liked, "like_cnt":like_cnt})


@csrf_exempt
def like_brand(request):
    req = json.loads(request.body)
    user_id = req["user_id"]
    brand_id = req["brand_id"]
    action = req["action"]

    user = get_object_or_404(User, id=user_id)
    brand = get_object_or_404(Brand, id=brand_id)

    if action == "on":
        BrandLike.objects.create(user=user, brand=brand)
    else:
        brand_like = get_object_or_404(BrandLike, user=user, brand=brand)
        brand_like.delete()

    return JsonResponse({"action":action})


@csrf_exempt
def search_for_brands(request):
    req = json.loads(request.body)
    keyword = req["keyword"]
    brands = Brand.objects.all().filter(name__icontains=keyword)

    return JsonResponse({"keyword":keyword, "brands":list(brands.values())}) # 각 brand object를 dictionary 형태로 변환