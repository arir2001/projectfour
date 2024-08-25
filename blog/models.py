from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager

# Post and comment models adapted from CodeInstitute Django Blog

STATUS = ((0, "Draft"), (1, "Published"), (2, "Archived"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name="blog_posts")

    featured_image = CloudinaryField('image', default='placeholder')

    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = TaggableManager(blank=True)

    mastimage = models.ImageField(upload_to='media/masthead_images/', blank=True, null=True, default='static/images/whiteboard.png')
    
    viewcount = models.PositiveIntegerField(default=0)  # View Count Field

    def __str__(self):
        return f"{self.title} | {self.author}"

    class Meta:
        ordering = ["-created_on"]




class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"