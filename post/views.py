from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .form import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Count


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.all()
    like_cnt = PostLike.objects.filter(post=post).count()
    comments_cnt = Comment.objects.filter(post=post).count()

    try:  # 로그인 한 상태일 때
        if PostLike.objects.filter(user=request.user, post=post).exists():
            is_liked = True
        else:
            is_liked = False

    except TypeError:  # 로그인 안 한 상태일 때
        is_liked = False
    ctx = {'post': post, 'comments': comments, "is_liked": is_liked,
           'like_cnt': like_cnt, 'comments_cnt': comments_cnt}

    return render(request, template_name='post/post_detail.html', context=ctx)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForm()
    ctx = {'form': form}

    return render(request, template_name='post/post_form.html', context=ctx)


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

        ctx = {'form': form, 'post': post}
        return render(request, template_name='post/post_form.html', context=ctx)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post:list')


@csrf_exempt
def like_post(request):
    req = json.loads(request.body)
    user_id = req["user_id"]
    post_id = req["post_id"]
    action = req["action"]

    user = get_object_or_404(User, id=user_id)
    post = get_object_or_404(Post, id=post_id)

    if action == "on":
        PostLike.objects.create(user=user, post=post)
    else:
        post_like = get_object_or_404(PostLike, user=user, post=post)
        post_like.delete()

    return JsonResponse({"action": action})


@csrf_exempt
def create_comment(request):
    req = json.loads(request.body)
    user_id = req['user_id']
    post_id = req['post_id']
    message = req['message']

    user = get_object_or_404(User, id=user_id)
    img_url = user.image.url
    post = get_object_or_404(Post, id=post_id)
    comment = Comment.objects.create(user=user, post=post, message=message)
    comment.save()

    return JsonResponse({'user': user.nickname, 'username': user.username, 'post_id': post_id, 'message': message, 'comment_id': comment.id, 'img_url':img_url})


@csrf_exempt
def update_comment(request):
    req = json.loads(request.body)
    post_id = req['post_id']
    comment_id = req['comment_id']
    message = req['message']

    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, post=post, id=comment_id)
    comment.message = message
    comment.save()

    return JsonResponse({'message': message, 'comment_id': comment_id})


@csrf_exempt
def delete_comment(request):
    req = json.loads(request.body)
    comment_id = req['id']

    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return JsonResponse({'id': comment_id})


def post_list(request):

    if request.GET.get('keyword'):
        keyword = request.GET.get('keyword')
        posts = Post.objects.filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword)).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    if request.GET.get('sort') == 'like':  # 좋아요 정렬 선택한 경우
        posts = posts.annotate(like_cnt=Count('postlike')) \
            .order_by('-like_cnt', '-created_at')
    elif request.GET.get('sort') == 'past':  # 과거순 정렬 선택한 경우
        posts = posts.order_by('created_at')
    elif request.GET.get('sort') == 'latest':  # 최신순 정렬 선택한 경우
        posts = posts.order_by('-created_at')

    paginator = Paginator(posts, 5)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    return render(request, 'post/list.html', locals())


def show_author_posts(request):
    author = get_object_or_404(User, username=request.GET.get('id'))
    posts = Post.objects.filter(user=author).order_by('-created_at')

    paginator = Paginator(posts, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    if author == request.user:
        return redirect('users:user_post')
    else:
        return render(request, 'post/author_posts.html', locals())
