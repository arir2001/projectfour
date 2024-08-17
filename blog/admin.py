from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Comment

# Register your models here.
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)