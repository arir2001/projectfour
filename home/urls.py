from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inquiry.html', views.inquiry, name='inquiry'),
    path('inquiries/', views.inquiry_list, name='inquiry_list'),
    path('inquiries/<int:inquiry_id>/archive/', views.archive_inquiry, name='archive_inquiry'),
    path('inquiries/<int:inquiry_id>/unarchive/', views.un_archive_inquiry, name='un_archive_inquiry'),
]

