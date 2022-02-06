from django.shortcuts import render, redirect, get_object_or_404
from .models import *
#from .form import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/list.html', locals())


@csrf_exempt
def search_for_posts(request):
    req = json.loads(request.body)  # need to learn how to deserialize queryset
    keyword = req["keyword"]
    posts = Post.objects.filter(title__icontains=keyword)
    print('hello')

    # 각 brand object를 dictionary 형태로 변환
    return JsonResponse({"keyword": keyword, "posts": list(posts.values())})
