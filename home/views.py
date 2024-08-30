from django.shortcuts import render, redirect, get_object_or_404
from home.models import Testimonial, CollaborateRequest, Inquire
from .forms import CollaborateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required
def inquiry_list(request):
    inquiries = CollaborateRequest.objects.filter(read=False)
    archived_inquiries = CollaborateRequest.objects.filter(read=True)
    return render(request, 'home/inquiryadminlist.html', 
    {'inquiries': inquiries,
     "archived_inquiries" : archived_inquiries})

def archive_inquiry(request, inquiry_id):
    inquiry = get_object_or_404(CollaborateRequest, pk=inquiry_id)
    inquiry.read = True
    inquiry.save()
    return redirect('inquiry_list')

def un_archive_inquiry(request, inquiry_id):
    inquiry = get_object_or_404(CollaborateRequest, pk=inquiry_id)
    inquiry.read = False
    inquiry.save()
    return redirect('inquiry_list')