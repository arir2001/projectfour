from django.shortcuts import render, redirect, get_object_or_404
from home.models import Testimonial, CollaborateRequest, Inquire
from .forms import CollaborateForm, TestimonialForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect

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


#testimonials
@login_required
def testimonialFormView(request):
    """View for users to submit testimonials"""
    if request.method == 'POST':
        form = TestimonialForm(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Your testimonial has been submitted successfully!')
            form = TestimonialForm()  
    else:
        form = TestimonialForm()  
    return render(request, 'home/submit_testimonial.html', {'form': form})  

#view to archive, publish the testimonial, redirected to the testimonial list
@login_required
@user_passes_test(lambda u: u.is_staff)
def testimonial_list(request):
    testimonials = Testimonial.objects.filter(status=1)
    unpublished_testimonials = Testimonial.objects.filter(status=0)
    archived_testimonials = Testimonial.objects.filter(status=3)
    return render(request, 'home/testimonial_list.html',  {
        'unpublished_testimonials': unpublished_testimonials,
        'testimonials': testimonials,
        'archived_testimonials': archived_testimonials,
    })

@login_required
@user_passes_test(lambda u: u.is_superuser)
def testimonial_delete(request, testimonial_id):
    """View to delete a testimonial"""
    post = get_object_or_404(Testimonial, id=testimonial_id) 
    referer_url = request.META.get('HTTP_REFERER', 'blog/user_admin/testimonials/')  
    post.delete()
    messages.success(request, 'Testimonial deleted!')

    return HttpResponseRedirect(referer_url)

def testimionail_publish_admin(request, testimonial_id):
    """View to approve or unapprove testimionaail """
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    referer_url = request.META.get('HTTP_REFERER', 'blog/user_admin/testimonials/')

    if request.user.is_superuser:
        testimonial.status = 1 if testimonial.status == 0 else 0  #if post status is 1, set it to 0, otherwise leave as 0
        testimonial.save() 
        messages.success(
         request, 'Testimonial published!'
         if testimonial.status == 1 else 'Testimonial unpublished!')
    return HttpResponseRedirect(referer_url)
