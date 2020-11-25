from django import forms
from .models import UrlMappings

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlMappings
        fields = ['original_url']