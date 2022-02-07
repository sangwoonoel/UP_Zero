from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .form import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


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
    post = get_object_or_404(Post, id=post_id)
    comment = Comment.objects.create(user=user, post=post, message=message)
    comment.save()

    return JsonResponse({'user': user.username, 'post_id': post_id, 'message': message, 'comment_id': comment.id})


@csrf_exempt
def delete_comment(request):
    req = json.loads(request.body)
    comment_id = req['id']

    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return JsonResponse({'id': comment_id})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/list.html', locals())


@csrf_exempt
def search_for_posts(request):
    req = json.loads(request.body)  # need to learn how to deserialize queryset
    keyword = req["keyword"]
    posts = Post.objects.filter(title__icontains=keyword)
    postlist = list(posts.values())  # 딕셔너리 포스트들이 들어있는 리스트

    for post in postlist:
        user = get_object_or_404(User, id=post['user_id'])
        i = get_object_or_404(Post, id=post['id'])
        post["username"] = user.username
        post["created_at"] = i.created_string
        print(post)

    # 각 brand object를 dictionary 형태로 변환
    return JsonResponse({"keyword": keyword, "posts": postlist})
