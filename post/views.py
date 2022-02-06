from django.shortcuts import render, redirect, get_object_or_404
from .models import *
#from .form import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from datetime import datetime, timedelta

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/list.html', locals())
