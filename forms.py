
from django import forms

from .models import Contact


class Contactforms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'username',
            'email',
            'service',
            'text',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'service': forms.Select(attrs={'class':'form-control', 'required':''}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
        }

        # Contactforms.email
        # Contactforms.service
        # Contactforms.text