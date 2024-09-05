from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Post and comment models adapted from CodeInstitute Django Blog

from django.shortcuts import render

#to see why csrf isnt working!
def csrf_failure(request, reason=""):
    return render(request, "blog/csrf_failure.html", {'reason': reason})


#creates list of posts for blog
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/post_list.html'
    paginate_by = 6


#allows search foor titles
def search_posts(request):
    queryset = Post.objects.filter(status=1)

    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()
        if searched:
            titles = queryset.filter(title__icontains=searched)
        else:
            titles = queryset.none()

        return render(
            request,
            "blog/search_posts.html",
            {'searched': searched, 'titles': titles}
        )
    return render(request, "blog/post_list.html")


#allows someone to view an individual post, its comments
def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    masthead_image = post.featured_image
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return redirect('blogpost', slug=post.slug)

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
        }
    )


#allows some one to edit their comment, and it becomes un approved again. 
def comment_edit(request, slug, comment_id):
    """View to edit comments"""
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
            messages.add_message(
             request, messages.SUCCESS,
             'Comment submitted and awaiting approval')

    return HttpResponseRedirect(reverse('blogpost', args=[slug]))


#allows someone to delete their comment. 
def comment_delete(request, comment_id, slug=None):
    """View to delete comment"""
    comment = get_object_or_404(Comment, pk=comment_id)
    referer_url = request.META.get(
             'HTTP_REFERER', reverse('blogpost', args=[slug])
         )
    if request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.add_message(
             request, messages.ERROR,
             'You can only delete your own comments!'
         )
    return HttpResponseRedirect(referer_url)


#login required to be super user. Approves a comment, or unapproves it. 
@login_required
@user_passes_test(lambda u: u.is_superuser)
def comment_approve(request, comment_id):
    """View to approve comment in user admin"""
    comment = get_object_or_404(Comment, pk=comment_id)
    referer_url = request.META.get('HTTP_REFERER')

    if not comment.approved and request.user.is_superuser:
        comment.approved = True
        comment.save()
        messages.success(request, 'Comment approved!')
    elif comment.approved and request.user.is_superuser:
        comment.approved = False
        comment.save()
        messages.success(request, 'Comment unapproved!')

    return HttpResponseRedirect(referer_url)


#show the comments in dashboard
@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_admin(request):
    """Show the comments and posts in admin"""
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
        }
    )


#allows management approvals.
@login_required
@user_passes_test(lambda u: u.is_superuser)
def comments_admin(request):
    """Manage comments in admin"""
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
        }
    )


#blog post creation, updating. Redirects to the post detail.
@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_or_update_post(request, slug=None):
    """Create or update a blog post"""
    if not request.user.is_superuser:
        return HttpResponseForbidden(
            "You are not allowed to access this page.")

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
            post.author = request.user
            post.save()
            messages.success(request, 'Post saved successfully!')
            return redirect('blogpost', slug=post.slug)
        messages.warning(request, 'Post not saved. Check form.')

    return render(request, 'blog/post_form.html', {'form': form})


#show the posts in dashboard
@login_required
@user_passes_test(lambda u: u.is_superuser)
def blogposts_admin(request):
    """Admin view for blog posts"""
    posts = Post.objects.all()
    return render(request, "blog/blogpostadmin.html", {"posts": posts})


#view to approve or unapprove. 
@login_required
@user_passes_test(lambda u: u.is_superuser)
def blog_publish_admin(request, slug):
    """View to approve or unapprove blog post"""
    post = get_object_or_404(Post, slug=slug)
    referer_url = request.META.get('HTTP_REFERER', '/blog/user_admin/')

    if request.user.is_superuser:
        post.status = 1 if post.status == 0 else 0  #if post status is 1, set it to 0, otherwise leave as 0
        post.save() 
        messages.success(
         request, 'Post published!'
         if post.status == 1 else 'Post unpublished!')
    return HttpResponseRedirect(referer_url)


#delete a blog post, redirect to user admin
@login_required
@user_passes_test(lambda u: u.is_superuser)
def post_delete(request, slug):
    """View to delete a blog post"""
    post = get_object_or_404(Post, slug=slug)
    referer_url = request.META.get('HTTP_REFERER', '/blog/user_admin/')
    post.delete()
    messages.success(request, 'Post deleted!')

    return HttpResponseRedirect(referer_url)
