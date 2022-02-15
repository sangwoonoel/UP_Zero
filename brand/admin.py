from django.contrib import admin
from .models import *

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    search_fields = ['name', 'category__name']
@admin.register(BrandLike)
class BrandLikeAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__nickname', 'brand__name']
admin.site.register(Category)