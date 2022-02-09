from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.main, name='main'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="log_out"),
    path("signup/", views.signup, name="signup"),
    path("mypage/", views.mypage, name="mypage"),
    path("user_post/", views.user_post, name="user_post"),
    path("brand_delete/", views.mypage_post_delete, name="mypage_post_delete"),
    path("post_delete/", views.mypage_brand_delete, name="mypage_brand_delete"),
    # path("user_post_delete/", views.user_post_delete, name="user_post_delete"),


    
    


    


]