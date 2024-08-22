from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='blogpost'),
    path('search_posts', views.search_posts, name='search-posts'),
    path('<slug:slug>/edit_comment/<int:comment_id>',views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',views.comment_delete, name='comment_delete'),
]

