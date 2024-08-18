from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Comment

# Register your models here.
#actions for comments. 
@admin.action(description="Mark selected comments as approved and show under blog post")
def make_published(modeladmin, request, queryset):
    queryset.update(approved=True)

@admin.action(description="Mark selected comments as unapproved and hide from view")
def unapprove(modeladmin, request, queryset):
    queryset.update(approved=False)

#actions for posts. 
@admin.action(description="Return the selected post(s) to drafts")
def re_draft(modeladmin, request, queryset):
    queryset.update(status = 0)

@admin.action(description="Publish the selected post(s)")
def publish(modeladmin, request, queryset):
    queryset.update(status = 1)

@admin.action(description="Archive the selected post(s)")
def archive(modeladmin, request, queryset):
    queryset.update(status = 2)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):    
    ordering = ['status', '-created_on']  # Order by status first, then created_on in descending order

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = [re_draft, archive, publish]
    

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('body', 'author', 'approved')
    actions = [make_published, unapprove]
    

