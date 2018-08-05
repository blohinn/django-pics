from django import forms
from django.forms import ModelForm
from .models import Photo


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'caption')
        widgets = {
            'photo': forms.HiddenInput(attrs={
                'role': 'uploadcare-uploader',
                'data-crop': '500x500 minimum',
                'data-images-only': 'true'
            }),
            'caption': forms.Textarea(attrs={
                'rows': 3
            }),
        }
