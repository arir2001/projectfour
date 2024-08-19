from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from home.models import Testimonial


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
    