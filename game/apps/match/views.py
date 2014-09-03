from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import ModelFormMixin
from .models import Match, Attack
from game.apps.characters.models import Character
from game.apps.enemies.models import Enemy
from .forms import CreateMatch, AttackForm
from .models import Spell
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from .helpers import calculate_player_damage, calculate_boss_damage, calculate_player_health,  calculate_boss_health, calculate_xp


class CreateMatch(CreateView):
    model = Match
    form_class = CreateMatch

    def get_context_data(self, **kwargs):
        context = super(CreateMatch, self).get_context_data(**kwargs)
        context['characters'] = Character.objects.filter(user=self.request.user)
        context['enemys'] = Enemy.objects.all()
        return context

    def form_valid(self, form):
        Form = form.save(commit=False)
        boss = form.cleaned_data['enemy']
        Form.enemy_health = calculate_boss_health(boss)
        Form.resource = 1
        character = form.cleaned_data['character']
        Form.character_health = calculate_player_health(character)
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)


class MatchDetail(DetailView):
    model = Match

    def get_context_data(self, **kwargs):
        context = super(MatchDetail, self).get_context_data(**kwargs)

        context['spells'] = Spell.objects.filter(
            type=self.object.character.type,
            level_required__lte=context['match'].character.level_data()['current_level'],
        )

        match = get_object_or_404(
            Match,
            pk=self.kwargs.get('pk'),
            character__user=self.request.user,
        )

        if self.object.enemy_health == 0:
            context['condition'] = "win"
        else:
            if self.object.character_health == 0:
                context['condition'] = "loose"
            else:
                pass

        context['match'] = match

        return context


class MatchList(ListView):
    model = Match


class AttackForm(CreateView):
    model = Attack
    form_class = AttackForm

    def get_context_data(self, **kwargs):
        context = super(AttackForm, self).get_context_data(**kwargs)
        match = get_object_or_404(
            Match,
            pk=self.kwargs.get('pk'),
            character__user=self.request.user
        )
        context['match'] = match
        return context

    def form_valid(self, form):
        spell = form.cleaned_data['spell']
        attackform = form.save(commit=False)
        match = Match.objects.get(id=self.kwargs['pk'])
        boss_spell = Spell.objects.filter(level_required__lte=match.enemy.level).order_by('?')[0]
        attackform.enemy_return_spell = boss_spell
        character = match
        attackform.selected_spell = spell

        cooldown = spell.turn_cooldown
        turn = 0
        attack_history_list = Attack.objects.filter(match=match).order_by('-time')[:cooldown]

        if attack_history_list:
            for attack_history in attack_history_list:
                if attack_history.spell != spell and attack_history:
                    if attack_history <= cooldown:
                        turn = turn + 1
                    else:
                        turn = cooldown
                else:
                    pass
        else:
            turn = cooldown

        if spell.level_required <= match.character.level_data()['current_level'] and spell.type == match.character.type and turn == cooldown:

            if match.finished is False:
                if match.character_health <= calculate_boss_damage(boss_spell, match):
                    match.character_health = 0
                    match.finished = True
                else:
                    if match.enemy_health <= calculate_player_damage(character, spell):
                        match.enemy_health = 0
                        match.character.xp = match.character.xp + calculate_xp(match)
                        match.finished = True
                    else:
                        match.character_health = match.character_health - calculate_boss_damage(boss_spell, match)
                        match.enemy_health = match.enemy_health - calculate_player_damage(character, spell)
            else:
                return super(ModelFormMixin, self).form_valid(form)

            attackform.damage_dealt = calculate_player_damage(match, spell)
            attackform.damage_taken = calculate_boss_damage(boss_spell, match)

            attackform.match = match
            attackform.time = now()
            match.save()
            match.character.save()
            self.object = attackform.save()

            return super(ModelFormMixin, self).form_valid(form)
        else:
            return super(ModelFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse('match:detail', kwargs={'pk': self.kwargs['pk']})
