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

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']