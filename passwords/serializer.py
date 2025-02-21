from django import forms
from .models import PasswordEntry

class PasswordFormSerializer(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = PasswordEntry
        fields = ['website', 'username', 'password']