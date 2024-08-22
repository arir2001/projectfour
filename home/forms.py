from .models import Inquire, CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'service', 'email', 'message',)
        widgets = {
            'service': forms.Select(),  #default widget will work fine here
        }


