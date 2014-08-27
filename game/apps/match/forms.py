from django import forms
from .models import Match, Attack


class CreateMatch(forms.ModelForm):

    class Meta:
        model = Match
        exclude = ['character_health', 'enemy_health', 'resource']


class AttackForm(forms.ModelForm):

    class Meta:
        model = Attack
        exclude = ['time', 'enemy_return_spell', 'match', 'damage_dealt', 'damage_taken']
