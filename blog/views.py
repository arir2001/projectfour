from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from blog.models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

def post_list(request, slug):
    # Get the post object by slug
    post = get_object_or_404(Post, slug=slug)

    # Increment the view count
    post.viewcount += 1
    post.save(update_fields=['viewscount'])

    # Render the template with the post
    return render(request, 'post_list.html', {'post': post})

class PostList(generic.ListView):
    model = Post