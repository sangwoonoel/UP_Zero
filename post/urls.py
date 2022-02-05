from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    #path('list/', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('update/<int:pk>/', views.post_update, name='post_update'),
    path('delete/<int:pk>/', views.post_update, name='post_delete'),
    path('like/', views.like_post, name='post_like'),
    # path('<int:pk>/create_comment/', views.create_comment, name='create_comment'),
    # path('<int:pk>/<int:pk>/delete_comment', views.delete_comment, name='delete_comment'),
]
