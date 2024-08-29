from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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

#deletes the comments from suepruser or author 
def comment_delete(request, comment_id, slug=None):
    """
    view to delete comment
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    referer_url = request.META.get('HTTP_REFERER', reverse('blogpost', args=[slug]))
    
    #request.user == comment.author or
    if  request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
    
    # Redirect back to the referring page or fallback to the blog post
    return HttpResponseRedirect(referer_url)

#deletes the comments from suepruser or author 
def comment_approve(request, comment_id):
    """
    view to approve comment in user admin
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    referer_url = request.META.get('HTTP_REFERER')

    if comment.approved == False: 
        if request.user.is_superuser:
            comment.approved = True
            comment.save() #save to daata base 
            messages.success(request, 'Comment approved!')
    elif comment.approved == True: 
        if request.user.is_superuser:
            comment.approved = False
            comment.save() #save to daata base 
            messages.success(request, 'Comment unapproved!')

        
    # Redirect back to the referring page or fallback to the blog post
    return HttpResponseRedirect(referer_url)

#shows the comments
def user_admin(request):
    posts = Post.objects.all()
    unapproved_comments = Comment.objects.filter(approved=False)
    approved_comments = Comment.objects.filter(approved=True)
    comments = Comment.objects.all()
    return render(
        request,
        "blog/dashboard.html",
        {
            "unapproved_comments": unapproved_comments,
            "approved_comments": approved_comments,
            "comments": comments,
            "posts": posts,
        },
    )

def comments_admin(request):
    unapproved_comments = Comment.objects.filter(approved=False)
    approved_comments = Comment.objects.filter(approved=True)
    comments = Comment.objects.all()
    return render(
        request,
        "blog/commentadmin.html",
        {
            "unapproved_comments": unapproved_comments,
            "approved_comments": approved_comments,
            "comments": comments,
        },)

def create_or_update_post(request, slug=None):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to access this page.")

    if slug:
        post = get_object_or_404(Post, slug=slug)
        form = PostForm(instance=post)
    else:
        post = None
        form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            messages.success(request, 'Post saved successfully!')
            return redirect('blogpost',  slug=post.slug)  #change to the correct view back too admin dashboard
        else:
            messages.warning(request, 'Post not saved. Check form.')

    return render(request, 'blog/post_form.html', {'form': form})

def blogposts_admin(request):
    posts = Post.objects.all()
    return render(
        request,
        "blog/blogpostadmin.html",
        {"posts": posts,},)

def blog_publish_admin(request, slug):
    """
    view to approve comment in user admin
    """

    post = get_object_or_404(Post, slug=slug)

    referer_url = request.META.get('HTTP_REFERER', '/blog/user_admin/')  # Provide a fallback URL

    # Toggle post status based on the current value
    if request.user.is_superuser:
        if post.status == 0:
            post.status = 1
            post.save()  # Save changes to the database
            messages.success(request, 'Post published!')
        elif post.status == 1:
            post.status = 0
            post.save()  # Save changes to the database
            messages.success(request, 'Post unpublished!')

    # Redirect back to the referring page or fallback to the blog post admin
    return HttpResponseRedirect(referer_url)

def post_delete(request, slug):
    """
    view to delete comment
    """
    post = get_object_or_404(Post, slug=slug)

    referer_url = request.META.get('HTTP_REFERER', '/blog/user_admin/')  # Provide a fallback URL

    #request.user == comment.author or
    post.delete()
    messages.success(request, 'Post deleted!')

    # Redirect back to the referring page or fallback to the blog post
    return HttpResponseRedirect(referer_url)