from django.urls import path
from .views import *

app_name = 'brand'

urlpatterns = [
    path('list/', show_list, name='list'),
    path('<int:pk>/', show_detail, name='detail'),
    path('wish/', wish_brand, name='wish'),
]