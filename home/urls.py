from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inquiry.html', views.inquiry, name='inquiry'),
    path('inquiries/', views.inquiry_list, name='inquiry_list'),
    path('inquiries/<int:inquiry_id>/archive/', views.archive_inquiry, name='archive_inquiry'),
    path('inquiries/<int:inquiry_id>/unarchive/', views.un_archive_inquiry, name='un_archive_inquiry'),
    path('submit-testimonial/', views.testimonialFormView, name='submit_testimonial'),
    path('blog/user_admin/testimonials/', views.testimonial_list, name='testimonial_list'),
    path('blog/user_admin/testimonials/delete_testimonial/<int:testimonial_id>/', views.testimonial_delete, name='delete_testimonial'),
    path('blog/user_admin/testimonials/draft_testimonial/<int:testimonial_id>/', views.testimionail_publish_admin, name='testimionail_publish_admin'),
    path('blog/user_admin/testimonials/publish_testimonial/<int:testimonial_id>/', views.testimionail_publish_admin, name='publish_testimonial_list'),
]

