from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.main, name='main'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="log_out"),
    path("signup/", views.signup, name="signup"),
    path("mypage/", views.mypage, name="mypage"),
    path("brand_like/", views.brand_like, name="brand_like"),
    path("post_like/", views.post_like, name="post_like"),
    path("user_post/", views.user_post, name="user_post"),
    path("comments_list/", views.comments_list, name="comments_list"),
    path("post_delete/", views.mypage_post_delete, name="mypage_post_delete"),
    path("brand_delete/", views.mypage_brand_delete, name="mypage_brand_delete"),
    path("mypage_comment_delete/", views.mypage_comment_delete, name="mypage_comment_delete"),
    # path("user_post_delete/", views.user_post_delete, name="user_post_delete"),

    
    


    


]