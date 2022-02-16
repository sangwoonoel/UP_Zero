from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from brand import views as brandview
import json
from django.http import JsonResponse

app_name = 'users'

extra_patterns = [
    path("", views.mypage, name="mypage"),
    path("brands/", views.brand_like, name="my_brand"),
    path("scraps/", views.post_like, name="my_scrap"),
    path("posts/", views.user_post, name="my_post"),
    path("comments/", views.comments_list, name="my_comment"),
    path("brand_delete/<int:pk>", views.mypage_brand_delete, name="mypage_brand_delete"),
]

urlpatterns = [
    path('', views.main, name='main'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path('mypage/', include(extra_patterns)),
    # path("mypage/home", views.mypage, name="mypage"),
    # path("mypage/brands/", views.brand_like, name="my_brand"),
    # path("mypage/scraps/", views.post_like, name="my_scrap"),
    # path("mypage/posts/", views.user_post, name="my_post"),
    # path("mypage/comments/", views.comments_list, name="my_comment"),
    # path("post_delete/", views.mypage_post_delete, name="mypage_post_delete"),
    # path("brand_delete/", views.mypage_brand_delete, name="mypage_brand_delete"),  
    # path("mypage_comment_delete/", views.mypage_comment_delete, name="mypage_comment_delete"),  
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.password, name='password'),
    path('forgot_id/', views.ForgotIDView, name="forgot_id"),
    # path("user_post_delete/", views.user_post_delete, name="user_post_delete")
]