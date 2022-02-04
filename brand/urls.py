from django.urls import path
from .views import *

app_name = 'brand'

urlpatterns = [
    path('list/', show_list, name='list'),
    path('<int:pk>/', show_detail, name='detail'),
    path('like/', like_brand, name='like'),
]