from django import forms
from .models import UrlMapping

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlMapping
        fields = ['original_url']