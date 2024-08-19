from django.shortcuts import render, get_object_or_404
from home.models import Testimonial

# Home view that lists published testimonials
def home(request):
    #get the published testimonials
    testimonials = Testimonial.objects.filter(status=1)

    return render(request, 'home/index.html', {'testimonials': testimonials})