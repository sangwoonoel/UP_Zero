from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('list/', views.post_list, name="list"),
    path('search/', views.search_for_posts, name='search'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('update/<int:pk>/', views.post_update, name='post_update'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('like/', views.like_post, name='post_like'),
    path('create_comment/', views.create_comment, name='create_comment'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
    path('update_comment/', views.update_comment, name='update_comment'),
]
