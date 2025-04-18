from django.contrib import admin
from .models import Comment, Like

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'user__username')
    date_hierarchy = 'created_at'

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)
    date_hierarchy = 'created_at'
