from django.contrib import admin

from .models import (
    Comment,
    Post,
    Tag
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'likes', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'post', )


admin.site.register(Tag)
