from django import forms
from .models import Dog

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'
        widgets = {
            'breed': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'favoritefood': forms.TextInput(attrs={'class': 'form-control'}),
            'favoritetoy': forms.TextInput(attrs={'class': 'form-control'}),
        }