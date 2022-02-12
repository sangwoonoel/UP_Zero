from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('update/', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('password/', views.password, name='password'),
    path('forgot_id/', views.ForgotIDView, name="forgot_id"),
    # path("user_post_delete/", views.user_post_delete, name="user_post_delete")
]