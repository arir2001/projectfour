from django.urls import path
from . import views

urlpatterns = [
    #blog and posts URLs
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='blogpost'),
    path('search_posts/', views.search_posts, name='search-posts'),
    
    #comment edit and delete comments urls
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('blog/user_admin/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete_admin'),
    path('blog/user_admin/approve_comment/<int:comment_id>/', views.comment_approve, name='comment_approve_admin'),

    #admin URLs
    path('blog/user_admin/', views.user_admin, name='admin'),
    path('blog/user_admin/comments', views.comments_admin, name='comments_admin'),
    path('blog/user_admin/comments/approve_comment/<int:comment_id>/', views.comment_approve, name='comment_approve_admin'),
    path('blog/user_admin/new_post/', views.create_or_update_post, name='create_post'),
    path('blog/user_admin/<slug:slug>/edit/', views.create_or_update_post, name='edit_post'),
]
