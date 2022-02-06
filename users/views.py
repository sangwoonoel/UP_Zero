from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm, SignupForm

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

def signup(request):
    
    if request.method =="POST":
       
        if User.objects.filter(username = request.POST['username']).exists():
            help_text = '이미 있는 아이디입니다.'
        

        elif len(request.POST['password1']) < 6:
            help_text = '비밀번호가 너무 간단합니다!'

        elif User.objects.filter(nickname = request.POST['nickname']).exists():
            help_text = '이미 있는 닉네임 입니다!'

        

        elif request.POST['password1'] != request.POST['password2']:
            help_text = '비밀번호가 일치하지 않습니다'

        elif User.objects.filter(email = request.POST['email']).exists():
            help_text = '이미 존재하는 이메일입니다.'
        else :
            user = User.objects.create_user(
                username= request.POST['username'],
                password = request.POST['password1'],
                email = request.POST['email'],
                nickname = request.POST['nickname']
            )
            

            return redirect ('users:main')
        ctx = {'help_text':help_text}
        return render(request, template_name='users/signup.html',context=ctx)
    else:
        return render(request, template_name='users/signup.html')

def main(request):
    return render(request, "base.html") # 나중에 users/main.html 로 수정