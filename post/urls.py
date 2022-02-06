from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('list/', views.post_list, name="list"),
    path('search/', views.search_for_posts, name='search'),
]
