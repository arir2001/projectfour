from django.shortcuts import render, redirect, get_object_or_404
from home.models import Testimonial, CollaborateRequest, Inquire
from .forms import CollaborateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

#index page
def home(request):
    testimonials = Testimonial.objects.filter(status=1)
    return render(request, 'home/index.html', {'testimonials': testimonials})


#inquiry form request -- allows users and non users to inquire.
def inquiry(request):
    collaborate_form = CollaborateForm()
    inquire = Inquire.objects.all()
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received! Response in 2 working days."
            )
            collaborate_form = CollaborateForm()

    return render(request, 'home/inquiry.html', {
        'collaborate_form': collaborate_form,
        'inquire': inquire
    })


#inquiry list for admin page-- allows archiving.  
@login_required
@user_passes_test(lambda u: u.is_staff)
def inquiry_list(request):
    inquiries = CollaborateRequest.objects.filter(read=False)
    archived_inquiries = CollaborateRequest.objects.filter(read=True)
    return render(request, 'home/inquiryadminlist.html', {
        'inquiries': inquiries,
        "archived_inquiries": archived_inquiries
    })


#view to archive the inquiry, redirected to the inquiry list
@login_required
@user_passes_test(lambda u: u.is_staff)
def archive_inquiry(request, inquiry_id):
    inquiry = get_object_or_404(CollaborateRequest, pk=inquiry_id)
    inquiry.read = True
    inquiry.save()
    return redirect('inquiry_list')


#view to unarchive the inquiry. 
@login_required
@user_passes_test(lambda u: u.is_staff)
def un_archive_inquiry(request, inquiry_id):
    inquiry = get_object_or_404(CollaborateRequest, pk=inquiry_id)
    inquiry.read = False
    inquiry.save()
    return redirect('inquiry_list')
