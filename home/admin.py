from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from home.models import Testimonial
from .models import Inquire, CollaborateRequest, Service

# Actions


@admin.action(description="Return the selected testimonial(s) to drafts")
def re_draft(modeladmin, request, queryset):
    queryset.update(status=0)


@admin.action(description="Publish the selected testimonial(s)")
def publish(modeladmin, request, queryset):
    queryset.update(status=1)


@admin.action(description="Archive the selected testimonial(s)")
def archive(modeladmin, request, queryset):
    queryset.update(status=2)


@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):
    list_display = ('name', 'extra_detail', 'service', 'status')
    actions = [re_draft, archive, publish]


# New code
@admin.register(Inquire)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'read', 'service')
