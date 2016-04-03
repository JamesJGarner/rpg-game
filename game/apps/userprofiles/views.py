from django.views.generic import UpdateView
from django.views.generic.edit import ModelFormMixin
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User
from game.apps.characters.models import Character
from game.apps.matches.models import Match, Attack
from game.apps.spells.models import SpellAcquired, Spell

class UserProfilePage(UpdateView):
    model = UserProfile
    success_url = '/settings/'
    form_class = UserProfileForm
    template_name = 'userprofile/UserProfile_form.html'

    def form_valid(self, form):
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserProfilePage, self).get_context_data(**kwargs)
        context['characters'] = Character.objects.filter(user=self.object.pk)

        wins = Match.objects.filter(character=self.object.pk, enemy_health=0).count()
        loses = Match.objects.filter(character=self.object.pk, character_health=0).count();

        total_damage_dealt = 0
        total_damage_taken = 0

        matches = Match.objects.filter(character=self.object.pk)
        for attack in Attack.objects.filter(match__in=matches):
            total_damage_dealt += attack.damage_dealt
            total_damage_taken += attack.damage_taken

        spell_used_list = {}
        for element in SpellAcquired.objects.filter(character=self.object.pk):
            spell_used_list[element.spell.name] = Attack.objects.filter(match__in=matches, spell=element.spell).count()

        most_used = max(spell_used_list, key=spell_used_list.get)
        most_used_spell = Spell.objects.get(name=most_used)

        context['wins'] = wins
        context['loses'] = loses
        context['percent_of_wins'] = str(round(float(wins - loses) / wins * 100, 1)) + "%";
        context['most_used_spell'] = most_used_spell
        context['total_damage_dealt'] = total_damage_dealt
        context['total_damage_taken'] = total_damage_taken
        return context
