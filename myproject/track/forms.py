from django import forms
from .models import Track

class TrackForm(forms.ModelForm):
    class Data:
        model = Track
        fields = ['name', 'description', 'duration', 'is_active']
        info = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter track name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter track description', 'rows': 3}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in weeks'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
