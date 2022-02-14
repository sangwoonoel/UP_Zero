from django.shortcuts import render, redirect
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

class LoginView(View):
    def get(self, request):
        #form = LoginForm()
        #return render(request, "accounts/login.html")
        next = None
        if request.GET.get("next"):
            next = request.GET.get("next")
        form = LoginForm()
        return render(request, "users/login.html", {"form": form, "next": next})

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
                if request.POST.get("next"):
                    return redirect(request.POST.get("next"))
                return redirect("/")

            return render(request, "users/login.html")

        ctx = {"form": form}
        return render(request, "users/login.html", ctx)

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

def signup(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            if re.findall('[ㄱ-ㅣ가-힣]', request.POST['username']) or re.findall('[`~!@#$%^&*(),<.>/?]+', request.POST['username']) or re.findall('[A-Z]', request.POST['username']):
                help_text = '아이디는 영문 소문자와 숫자만 가능합니다'
            elif len(request.POST['password']) < 8 or len(request.POST['password']) > 21 or not re.findall('[0-9]+', request.POST['password']) or \
    re.findall('[ㄱ-ㅣ가-힣]', request.POST['password']) or not re.findall('[`~!@#$%^&*(),<.>/?]+', request.POST['password']):
                help_text = '영문 대소문자, 숫자, 한 개 이상의 특수문자를 조합해서 8~21자리 비밀번호를 만들어주세요.'
            elif request.POST['password'] != request.POST['password2']:
                help_text = '비밀번호가 일치하지 않습니다!'

            else:
                user = User.objects.create_user(
                username= request.POST['username'],
                password = request.POST['password'],
                email = request.POST['email'],
                nickname = request.POST['nickname']
            )
                # auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # messages.success(request, f"{user.username}님의 회원 가입을 축하합니다!" )
                return render(request, 'users/first_login.html')

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
    # BrandLikes = BrandLike.objects.filter(user__id=request.user.pk)
    # # PostLikes = PostLike.objects.filter(user__id=request.user.pk)
    # # Comments = Comment.objects.filter(user__id=request.user.pk)

    # context = {'BrandLikes' :  BrandLikes}

    return render(request, 'users/mypage.html')

@login_required
def brand_like(request):
    # TODO : 클래스를 제외한 인스턴스는, 소문자 네이밍을 사용하는게 좋습니다.
    # brand_likes
    BrandLikes = BrandLike.objects.filter(user__id=request.user.pk)

    context = {'BrandLikes' : BrandLikes}

    return render(request, 'users/my_brand.html', context)

@login_required
def post_like(request):
    # TODO : 클래스를 제외한 인스턴스는, 소문자 네이밍을 사용하는게 좋습니다.
    PostLikes = PostLike.objects.filter(user__id=request.user.pk)

    context = {'PostLikes' : PostLikes}

    return render(request, 'users/my_scrap.html', context)




@login_required
def user_post(request):
    # TODO : 클래스를 제외한 인스턴스는, 소문자 네이밍을 사용하는게 좋습니다.
    MyPosts = Post.objects.filter(user__id=request.user.pk)

    context = {'MyPosts' : MyPosts}

    return render(request, 'users/my_post.html', context)

@login_required
def comments_list(request):
    # TODO : 클래스를 제외한 인스턴스는, 소문자 네이밍을 사용하는게 좋습니다.
    Comments = Comment.objects.filter(user__id=request.user.pk)

    context = {'Comments' : Comments}

    return render(request, 'users/my_comment.html', context)

def mypage_brand_delete(request):
    # TODO : 클래스를 제외한 인스턴스는, 소문자 네이밍을 사용하는게 좋습니다.
    BrandLikes = BrandLike.objects.filter(user__id=request.user.pk)

    # 첫 번째 브랜드 좋아요만 지우는 이유가 있나요?
    BrandLikes[0].delete()


    return redirect('users:mypage')


# def mypage_brand_delete(request):
#     brand = BrandLike.objects.filter(user__id=request.user.pk)
#     BrandLikes = BrandLike.objects.filter(brand__id=brand.id)

#     print(BrandLikes)
#     context = {'BrandLikes' : BrandLikes}

#     return render(request, 'users/brand_like.html', context)


def mypage_post_delete(request):
    PostLikes = PostLike.objects.filter(user__id=request.user.pk)
    PostLikes[0].delete()


    return redirect('users:mypage')

def mypage_comment_delete(request):
    Comments = Comment.objects.filter(user__id=request.user.pk)
    print(Comments)
    Comments[0].delete()
    return redirect('users:mypage')

# def user_post_delete(request):
#     MyPosts = Post.objects.filter(user__id=request.user.pk)
#     MyPosts[0].delete()
#     return redirect('users:mypage')

from django.template.loader import render_to_string

@unauthenticated_user
def ForgotIDView(request):
	context = {}
	if request.method == 'POST':
		email = request.POST.get('email')

		try:
			user = User.objects.get(email=email)
			if user is not None:
				template = render_to_string('users/email_template.html', {'name': user.nickname, 'id':user.username})
				method_email = EmailMessage(
					'Your ID is in the email',
					template,
					settings.EMAIL_HOST_USER,
					[email],
					)
				method_email.send(fail_silently=False)
				return render(request, 'users/id_sent.html', context)
		except:
			messages.info(request, "There is no username along with the email")
	context = {}
	return render(request, 'users/forgot_id.html', context)


#

#정보 수정
@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('users:mypage')
    else:
        user_change_form = CustomUserChangeForm(instance = request.user)
        return render(request, 'users/update.html', {'user_change_form':user_change_form})

@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/')
    return render(request, 'users/delete.html')


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)

        # 키워드인자명을 함께 써줘도 가능
        # password_change_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return redirect('users:mypage')

    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'users/password.html',{'password_change_form':password_change_form})
