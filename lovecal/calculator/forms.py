from django import forms
from .models import Valentine

class Valentineform(forms.ModelForm):
    class Meta:
        model=Valentine
        fields=('crush','name')