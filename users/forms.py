from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, label = "아이디")
    password = forms.CharField(widget=forms.PasswordInput, label = "비밀번호")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                raise forms.ValidationError("password is wrong!!!")
        except User.DoesNotExist:
            raise forms.ValidationError("No User!!!")

class SignUpForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput, label = "비밀번호확인")

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'nickname']

        labels = {
                'username': '제목',
                'password': '비밀번호',
                'password2': '비밀번호확인',
                'email': '이메일',
                'nickname': '닉네임',
            }
        
       



