from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag
def get_recent_blog_posts(count=1):
    return Post.objects.filter(status=1).order_by('-created_on')[:count]