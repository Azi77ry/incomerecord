from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['date', 'amount', 'description']
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',  # Use HTML5 date input
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',  # Allow decimal values
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }