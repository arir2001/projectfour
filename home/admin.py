from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from home.models import Testimonial
from .models import Inquire, CollaborateRequest, Service

#actions. 
@admin.action(description="Return the selected testimonials(s) to drafts")
def re_draft(modeladmin, request, queryset):
    queryset.update(status = 0)

@admin.action(description="Publish the selected testimonials(s)")
def publish(modeladmin, request, queryset):
    queryset.update(status = 1)

@admin.action(description="Archive the selected testimonials(s)")
def archive(modeladmin, request, queryset):
    queryset.update(status = 2)

@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):    
    list_display = ('name', 'extra_detail', 'service', 'status')
    actions = [re_draft, archive, publish]

#new code
@admin.register(Inquire)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Customize the display in the admin list view
    search_fields = ('name',)  # Add a search box to search by name

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'read', 'service')