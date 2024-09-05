from .models import CollaborateRequest, Testimonial
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'service', 'email', 'message',)
        widgets = {
            'service': forms.Select(), 
        }


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('name', 'age', 'extra_detail', 'testimonial', 'service')  
        widgets = {
            'service': forms.Select(),  
        }
