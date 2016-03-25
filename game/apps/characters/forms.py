from django import forms
from .models import Character
from game.apps.matches.models import Match

class CharacterCreate(forms.ModelForm):
    error_css_class = "error"

    class Meta:
        model = Character
        exclude = ['user', 'health', 'xp']


class CreateMatch(forms.ModelForm):

    class Meta:
        model = Match
        exclude = ['character_health', 'enemy_health', 'resource', 'character']

