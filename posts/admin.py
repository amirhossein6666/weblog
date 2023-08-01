from django.contrib import admin

from .models import Post , Comment


class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text', ]
    extra = 0


class PostAdmin(admin.ModelAdmin):
    List_display = ['title', 'is_enable', 'publish_date', 'created_time']
    inlines = [CommentAdminInline, ]


admin.site.register(Post, PostAdmin)
# admin.site.register(Comment)