from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    search_fields = ['title', 'user__username', 'user__nickname']
@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user']
    search_fields = ['post__title', 'user__username', 'user__nickname']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']
    search_fields = ['user__username', 'user__nickname', 'post__title']