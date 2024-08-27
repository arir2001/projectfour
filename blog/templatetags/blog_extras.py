from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag
def get_recent_blog_posts(count=1):
    return Post.objects.filter(status=1).order_by('-created_on')[:count]


@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter(name='add_type')
def add_type(field,input_type):
    return field.as_widget(attrs={"type": input_type})