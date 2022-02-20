from django.template.loader import render_to_string
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages, auth
from django.views import View
from django.conf import settings
from django.core.mail import EmailMessage
from .decorators import unauthenticated_user
from brand.models import *
from post.models import *
from .models import User
from .forms import LoginForm, SignUpForm, CustomUserChangeForm
import re
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q


# class LoginView(View):
#     def get(self, request):
#         #form = LoginForm()
#         #return render(request, "accounts/login.html")
#         next = None
#         if request.GET.get("next"):
#             next = request.GET.get("next")
#         form = LoginForm()
#         return render(request, "users/login.html", {"form": form, "next": next})

#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 # print(user.pk)
#                 # print(user.username)
#                 # print(user.user_score)
#                 if request.POST.get("next"):
#                     return redirect(request.POST.get("next"))
#                 return redirect("/")

#             return render(request, "users/login.html")

#         ctx = {"form": form}
#         return render(request, "users/login.html", ctx)

# def log_out(request):
#     logout(request)
# return redirect("users:main")

# def signup(request):
#     if request.method =="POST":

#         if User.objects.filter(username = request.POST['username']).exists():
#             help_text = '이미 있는 아이디입니다.'


#         elif len(request.POST['password1']) < 6:
#             help_text = '비밀번호가 너무 간단합니다!'

#         elif User.objects.filter(nickname = request.POST['nickname']).exists():
#             help_text = '이미 있는 닉네임 입니다!'


#         elif request.POST['password1'] != request.POST['password2']:
#             help_text = '비밀번호가 일치하지 않습니다'

#         elif User.objects.filter(email = request.POST['email']).exists():
#             help_text = '이미 존재하는 이메일입니다.'
#         else :
#             user = User.objects.create_user(
#                 username= request.POST['username'],
#                 password = request.POST['password'],
#                 email = request.POST['email'],
#                 nickname = request.POST['nickname']
#             )
#             auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             messages.success(request, f"{user.username}님의 회원 가입을 축하합니다!" )
#             return redirect('/')

#         form = SignUpForm()
#         ctx = {'help_text':help_text, 'form':form}
#         return render(request, template_name='users/signup.html',context=ctx)

#     else:
#         form = SignUpForm()
#         ctx = {'form':form}
#         return render(request, template_name='users/signup.html', context=ctx)
# def signup(request):
#     if request.method =="POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             if request.POST['password'] != request.POST['password2'] and len(request.POST['password']) < 8:
#                 help_text = '비밀번호가 일치하지 않습니다! 비밀번호는 8자리 이상이어야합니다!'
#             elif len(request.POST['password']) < 8:
#                 help_text = '비밀번호는 8자리 이상이어야합니다!'
#             elif request.POST['password'] != request.POST['password2']:
#                 help_text = '비밀번호가 일치하지 않습니다!'
#             else:
#                 user = User.objects.create_user(
#                 username= request.POST['username'],
#                 password = request.POST['password'],
#                 email = request.POST['email'],
#                 nickname = request.POST['nickname']
#             )
#                 auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#                 messages.success(request, f"{user.username}님의 회원 가입을 축하합니다!" )
#                 return redirect('/')
#             context = {'form': form, 'help_text': help_text}
#             return render(request, 'users/signup.html', context)
#     else:

#         form = SignUpForm()
#     context = {'form': form}
#     return render(request, 'users/signup.html', context)

# def signup(request):
#     if request.method =="POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             if re.findall('[ㄱ-ㅣ가-힣]', request.POST['username']) or re.findall('[`~!@#$%^&*(),<.>/?]+', request.POST['username']) or re.findall('[A-Z]', request.POST['username']):
#                 help_text = '아이디는 영문 소문자와 숫자만 가능합니다'
#             elif len(request.POST['password']) < 8 or len(request.POST['password']) > 21 or not re.findall('[0-9]+', request.POST['password']) or \
#     re.findall('[ㄱ-ㅣ가-힣]', request.POST['password']) or not re.findall('[`~!@#$%^&*(),<.>/?]+', request.POST['password']):
#                 help_text = '영문 대소문자, 숫자, 한 개 이상의 특수문자를 조합해서 8~21자리 비밀번호를 만들어주세요.'
#             elif request.POST['password'] != request.POST['password2']:
#                 help_text = '비밀번호가 일치하지 않습니다!'

#             else:
#                 user = User.objects.create_user(
#                 username= request.POST['username'],
#                 password = request.POST['password'],
#                 email = request.POST['email'],
#                 nickname = request.POST['nickname']
#             )
#                 # auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#                 # messages.success(request, f"{user.username}님의 회원 가입을 축하합니다!" )
#                 return render(request, 'users/first_login.html')

#             context = {'form': form, 'help_text': help_text}
#             return render(request, 'users/signup.html', context)
#     else:

#         form = SignUpForm()
#     context = {'form': form}
#     return render(request, 'users/signup.html', context)


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            if re.findall('[ㄱ-ㅣ가-힣]', request.POST['username']) or re.findall('[`~!@#$%^&*(),<.>/?]+', request.POST['username']) or re.findall('[A-Z]', request.POST['username']):
                help_text = '아이디는 영문 소문자와 숫자만 가능합니다'
            else:
                form.save()
                return render(request, 'users/first_login.html')
            context = {'form': form, 'help_text': help_text}
            return render(request, 'users/signup.html', context)
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def main(request):
    return render(request, "users/main.html")


@login_required
def mypage(request):
    # devs = Devtool.objects.get(id=pk)
    # idea = Devtool.idea_set.objects.filter(devtool='')

    # BrandLikes = PostLike.objects.filter(user = pk)
    # BrandLikes = BrandLike.objects.filter(user__id=request.user.pk)
    # # PostLikes = PostLike.objects.filter(user__id=request.user.pk)
    # # Comments = Comment.objects.filter(user__id=request.user.pk)

    # context = {'BrandLikes' :  BrandLikes}

    return render(request, 'users/mypage.html')


@login_required
def brand_like(request):
    BrandLikes = BrandLike.objects.filter(
        user__id=request.user.pk).order_by('-id')

    context = {'BrandLikes': BrandLikes}

    return render(request, 'users/my_brand.html', context)


@login_required
def post_like(request):

    q = Q()

    LikePosts = PostLike.objects.filter(
        user__id=request.user.pk).order_by('-id')

    post = Post.objects.filter(
        user__id=request.user.pk)

    if request.GET.get('keyword'):
        keyword = request.GET.get('keyword')
        q.add(Q(user__id=request.user.pk), q.AND)
        q.add(Q(title__icontains=keyword) | Q(
            content__icontains=keyword), q.AND)

        PostLikes = PostLike.objects.filter(q).order_by('-created_at')
    else:
        PostLikes = PostLike.objects.filter(
            user__id=request.user.pk).order_by('-id')

    if request.GET.get('sort') == 'like':  # 좋아요 정렬 선택한 경우
        PostLikes = PostLikes.annotate(like_cnt=Count('postlike')) \
            .order_by('-like_cnt', '-created_at')
    elif request.GET.get('sort') == 'past':  # 과거순 정렬 선택한 경우
        PostLikes = PostLikes.order_by('created_at')
    elif request.GET.get('sort') == 'latest':  # 최신순 정렬 선택한 경우
        PostLikes = PostLikes.order_by('-created_at')

    paginator = Paginator(PostLikes, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    cnt = PostLikes.count()
    total_post_cnt = post.count()
    total_like_cnt = LikePosts.count()

    return render(request, 'users/my_scrap.html', locals())


# @login_required
# def user_post(request):
#     MyPosts = Post.objects.filter(user__id=request.user.pk).order_by('-created_at')

#     context = {'MyPosts' : MyPosts}

#     return render(request, 'users/my_post.html', context)

@login_required
def user_post(request):

    q = Q()
    LikePosts = PostLikes = PostLike.objects.filter(
        user__id=request.user.pk).order_by('-id')

    post = Post.objects.filter(
        user__id=request.user.pk)

    if request.GET.get('keyword'):
        keyword = request.GET.get('keyword')
        q.add(Q(user__id=request.user.pk), q.AND)
        q.add(Q(title__icontains=keyword) | Q(
            content__icontains=keyword), q.AND)
        MyPosts = Post.objects.filter(q).order_by('-created_at')
    else:
        MyPosts = Post.objects.filter(
            user__id=request.user.pk).order_by('-created_at')

    if request.GET.get('sort') == 'like':  # 좋아요 정렬 선택한 경우
        MyPosts = MyPosts.annotate(like_cnt=Count('postlike')) \
            .order_by('-like_cnt', '-created_at')
    elif request.GET.get('sort') == 'past':  # 과거순 정렬 선택한 경우
        MyPosts = MyPosts.order_by('created_at')
    elif request.GET.get('sort') == 'latest':  # 최신순 정렬 선택한 경우
        MyPosts = MyPosts.order_by('-created_at')

    paginator = Paginator(MyPosts, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    cnt = MyPosts.count()
    total_post_cnt = post.count()
    total_like_cnt = LikePosts.count()

    return render(request, 'users/my_post.html', locals())


@login_required
def comments_list(request):
    Comments = Comment.objects.filter(
        user__id=request.user.pk).order_by('-created_at')

    context = {'Comments': Comments}

    return render(request, 'users/my_comment.html', context)


# def mypage_brand_delete(request):
#     brand = BrandLike.objects.filter(user__id=request.user.pk)
#     BrandLikes = BrandLike.objects.filter(brand__id=brand.id)

#     print(BrandLikes)
#     context = {'BrandLikes' : BrandLikes}

#     return render(request, 'users/brand_like.html', context)

def mypage_brand_delete(request, pk):
    brandlike = get_object_or_404(BrandLike, id=pk)
    brandlike.delete()
    return redirect('users:my_brand')


def mypage_scrap_delete(request, pk):
    postlike = get_object_or_404(PostLike, id=pk)
    postlike.delete()
    return redirect('users:my_scrap')


def mypage_comment_delete(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    comment.delete()
    return redirect('users:my_comment')


def mypage_post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('users:my_post')

# def user_post_delete(request):
#     MyPosts = Post.objects.filter(user__id=request.user.pk)
#     MyPosts[0].delete()
#     return redirect('users:mypage')


@unauthenticated_user
def ForgotIDView(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
            if user is not None:
                template = render_to_string(
                    'users/email_template.html', {'name': user.nickname, 'id': user.username})
                method_email = EmailMessage(
                    '[SLOW:NIQUE] 아이디 찾기 안내',
                    template,
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                method_email.send(fail_silently=False)
                return render(request, 'users/id_sent.html', context)
        except:
            messages.warning(request, '등록되지 않은 이메일입니다.')
    context = {}
    return render(request, 'users/forgot_id.html', context)


#

# 정보 수정
@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(
            request.POST, request.FILES, instance=request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '정보가 수정되었습니다.')
            return redirect('users:mypage')

        else:
            ctx = {'user_change_form': user_change_form}
            return render(request, 'users/update.html', ctx)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        return render(request, 'users/update.html', {'user_change_form': user_change_form})


@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/')
    return render(request, 'users/delete.html')


@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        # 키워드인자명을 함께 써줘도 가능
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호가 변경되었습니다.')
            return redirect('users:mypage')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password.html', {'form': form})


def forbid_access(request):
    return render(request, 'forbidden.html')
