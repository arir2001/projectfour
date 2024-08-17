from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Post
from django.utils import timezone

def post_view(request, slug):
    # Get the post object by slug
    post = get_object_or_404(Post, slug=slug)

    # Increment the view count
    post.viewcount += 1
    post.save(update_fields=['viewscount'])

    # Render the template with the post
    return render(request, 'post_detail.html', {'post': post})