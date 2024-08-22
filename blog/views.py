from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('blogpost', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('blogpost', args=[slug]))