from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm
from django.db.models import Q

# Create your views here.
# Post and comment models adapted from CodeInstitute Django Blog
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/post_list.html'
    paginate_by = 6

def search_posts(request):
    queryset = Post.objects.filter(status=1)
    if request.method == "POST":
        searched = request.POST.get('searched', '')
        titles = queryset.filter(title__icontains=searched)
        return 

        render(
            request, 
            "blog/search_posts.html", 
            {'searched': searched,
            'titles': titles,
            })
    else:         
        return render(request, "blog/post_list.html", {})

        

def post_detail(request, slug):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    masthead_image = post.mastimage
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request") 
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
             #create comment object but don't save yet
            comment = comment_form.save(commit=False)
             #assign the post to the comment
            comment.author = request.user
            #set comment to waiting for approval
            comment.post = post
            #save the comment
            comment.save()

             #redirect to the same post after saving the comment to avoid duplication on refresh
            return redirect('blogpost',  slug=post.slug)
            print("Received a comment request") 
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )
    
    comment_form = CommentForm()
    

    return render(
        request,
        "blog/blogpost.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "mastimage": masthead_image,
        },
    )