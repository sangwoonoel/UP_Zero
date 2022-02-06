from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.main, name='main'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="log_out"),
    path("signup/", views.signup, name="signup"),
]