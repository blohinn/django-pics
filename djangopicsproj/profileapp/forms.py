from django import forms
from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'first_name', 'last_name', 'bio')
        widgets = {
            'avatar': forms.HiddenInput(attrs={
                'role': 'uploadcare-uploader',
                'data-crop': '500x500 minimum',
                'data-images-only': 'true'
            }),
            'bio': forms.Textarea(attrs={
                'rows': 3
            }),
        }
