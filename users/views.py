from django.shortcuts import render, redirect, get_object_or_404

from brand.models import BrandLike, Brand, Category
from post.models import *
import users
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm, SignUpForm
from django.contrib import messages,auth
import re
from django.contrib.auth.decorators import login_required


class LoginView(View):
    def get(self, request):
        #form = LoginForm()
        #return render(request, "accounts/login.html")
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # print(user.pk)
                # print(user.username)
                # print(user.user_score)
                return render(request, "users/main.html")

            return render(request, "users/login.html")

        ctx = {"form": form}
        return render(request, "users/login.html", ctx)

def log_out(request):
    logout(request)
    return redirect("users:main")

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

def signup(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            if re.findall('[ㄱ-ㅣ가-힣]', request.POST['username']) or re.findall('[`~!@#$%^&*(),<.>/?]+', request.POST['username']) or re.findall('[A-Z]', request.POST['username']):
                help_text = '아이디는 영문 소문자와 숫자만 가능합니다'
            elif len(request.POST['password']) < 8 or len(request.POST['password']) > 21 or not re.findall('[0-9]+', request.POST['password']) or \
    re.findall('[ㄱ-ㅣ가-힣]', request.POST['password']) or not re.findall('[`~!@#$%^&*(),<.>/?]+', request.POST['password']):
                help_text = '영문 대소문자, 숫자, 한 개 이상의 특수문자를 조합해서 8~21자리 비밀번호를 만들어주세요.'
                
        
            else:
                user = User.objects.create_user(
                username= request.POST['username'],
                password = request.POST['password'],
                email = request.POST['email'],
                nickname = request.POST['nickname']
            )
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, f"{user.username}님의 회원 가입을 축하합니다!" )
                return redirect('/')
            context = {'form': form, 'help_text': help_text}
            return render(request, 'users/signup.html', context)
    else:
        
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'users/signup.html', context)

def main(request):
    return render(request, "users/main.html")

@login_required
def mypage(request):
    # devs = Devtool.objects.get(id=pk)
    # idea = Devtool.idea_set.objects.filter(devtool='')
    
    # BrandLikes = PostLike.objects.filter(user = pk)
    BrandLikes = BrandLike.objects.filter(user__id=request.user.pk)
    PostLikes = PostLike.objects.filter(user__id=request.user.pk)

    context = {'BrandLikes' :  BrandLikes, 'PostLikes' : PostLikes}

    return render(request, 'users/mypage.html', context)

@login_required
def user_post(request):
    # devs = Devtool.objects.get(id=pk)
    # idea = Devtool.idea_set.objects.filter(devtool='')
    
    # BrandLikes = PostLike.objects.filter(user = pk)
    
    MyPosts = Post.objects.filter(user__id=request.user.pk)
    
    context = {'MyPosts' : MyPosts}

    return render(request, 'users/user_post.html', context)

def mypage_brand_delete(request):
    BrandLikes = BrandLike.objects.filter(user__id=request.user.pk)
    BrandLikes[0].delete()
    
    
    return redirect('users:mypage')

def mypage_post_delete(request):
    PostLikes = PostLike.objects.filter(user__id=request.user.pk)
    PostLikes[0].delete()
    
    
    return redirect('users:mypage')

# def user_post_delete(request):
#     MyPosts = Post.objects.filter(user__id=request.user.pk)
#     MyPosts[0].delete()
#     return redirect('users:mypage')

from django.core.mail.message import EmailMessage

def send_email(request):
    subject = "message"
    to = ["id@gmail.com"]
    from_email = "id@gmail.com"
    message = "메지시 테스트"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()


