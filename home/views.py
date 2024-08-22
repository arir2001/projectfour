from django.shortcuts import render, get_object_or_404
from home.models import Testimonial, CollaborateRequest, Inquire
from .forms import CollaborateForm
from django.contrib import messages

# Home view that lists published testimonials
def home(request):
    #get the published testimonials
    testimonials = Testimonial.objects.filter(status=1)
    return render(request, 'home/index.html', {'testimonials': testimonials})

def inquiry(request):
    collaborate_form = CollaborateForm()
    inquire = Inquire.objects.all()
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")
            collaborate_form = CollaborateForm()

    return render(request, 'home/inquiry.html', 
    {'collaborate_form': collaborate_form,
        'inquire': inquire
    })