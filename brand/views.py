from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import *

def show_list(request, cate=None):
    if not cate:
        brands = Brand.objects.all()
    else: # 카테고리 선택한 경우
        brands = Brand.objects.filter(category__name=cate)
        cate = get_object_or_404(Category, name=cate).name_ko # 카테고리 국문명
        
    return render(request, 'brand/list.html', {'cate': cate, 'brands': brands})

def show_search_results(request):
    keyword = request.GET.get('keyword')
    brands = Brand.objects.filter(name__icontains=keyword)
    return render(request, 'brand/search-results.html', {'brands': brands})

def show_detail(request, pk):
    brand = get_object_or_404(Brand, pk=pk)

    try: # 로그인 상태
        if BrandLike.objects.filter(user=request.user, brand=brand).exists():
            is_liked = True
        else:
            is_liked = False
    except TypeError: # 로그인 안 한 상태
        is_liked = False
        
    return render(request, 'brand/detail.html', {'brand':brand, 'is_liked':is_liked})


@csrf_exempt
def like_brand(request):
    req = json.loads(request.body)
    user_id = req['user_id']
    brand_id = req['brand_id']
    action = req['action']

    user = get_object_or_404(User, id=user_id)
    brand = get_object_or_404(Brand, id=brand_id)

    if action == 'on':
        BrandLike.objects.create(user=user, brand=brand)
    else:
        get_object_or_404(BrandLike, user=user, brand=brand).delete()

    return JsonResponse({'action':action})