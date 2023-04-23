from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'author', 'like_count']}),
        ('Context', {'fields': ['text']})
    ]
    readonly_fields = ['is_popular', 'like_count']
    list_display = ['title', 'author', 'like_count', 'is_popular']
    list_filter = ['title', 'author', 'like_count']
    search_fields = ['title', 'author', 'text']
