from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inquiry.html', views.inquiry, name='inquiry'),
]