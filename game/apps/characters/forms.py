from django import forms
from .models import Character


class CharacterCreate(forms.ModelForm):
    error_css_class = "error"

    class Meta:
        model = Character
        exclude = ['user', 'health', 'xp']
