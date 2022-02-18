from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import *

def show_list(request):
    brands = Brand.objects.order_by('name')
    cate = None

    if request.GET.get('category'): # 카테고리 선택한 경우
        cate_id = int(request.GET.get('category'))
        brands = brands.filter(category__id=cate_id)
        cate = get_object_or_404(Category, id=cate_id) # 선택한 카테고리

    if request.GET.get('sort') == 'like': # 좋아요 정렬 선택한 경우
        brands = brands.annotate(like_cnt=Count('brandlike')) \
            .order_by('-like_cnt')

    paginator = Paginator(brands, 12)
    page = request.GET.get('page', 1)
    paginated_brands = paginator.get_page(page)

    cates = Category.objects.all() # for brand/navbar.html
    return render(request, 'brand/list.html', locals())


def show_search_results(request):
    keyword = request.GET.get('keyword')
    brands = Brand.objects.filter(name__icontains=keyword).order_by('name')

    cates = Category.objects.all() # for brand/navbar.html
    return render(request, 'brand/search-results.html', {'brands': brands, 'cates': cates})


def show_detail(request, pk):
    brand = get_object_or_404(Brand, pk=pk)

    if request.user.is_authenticated:
        if BrandLike.objects.filter(user=request.user, brand=brand).exists():
            is_liked = 'true'
        else:
            is_liked = 'false'
    else:
        is_liked = 'false'
    
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