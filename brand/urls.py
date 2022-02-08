from django.urls import path
from .views import *

app_name = 'brand'

urlpatterns = [
    path('list/', show_list, name='all'),
    path('list/<str:cate>', show_list, name='category'),

    path('search/', show_search_results, name='search'),
    path('<int:pk>/', show_detail, name='detail'),

    # URLs for Ajax
    path('like/', like_brand, name='like'),
]