from django import forms

from .models import Profession, Human
import re
from django.core.exceptions import ValidationError

class HumanForm(forms.ModelForm):

    def clean_title(self):
        title=self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValueError('Все плохо, мы все умрем!')
        return title

    class Meta():
        model = Human
        fields=['fname','lname','hage','passp','profs']
        widgets={
            'fname': forms.TextInput(attrs={'class':'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'hage': forms.TextInput(attrs={'class': 'form-control'}),
            'passp': forms.TextInput(attrs={'class': 'form-control'}),
            'profs': forms.Select(attrs={'class':'form-control'}),
        }