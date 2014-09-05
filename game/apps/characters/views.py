from django.views.generic import DetailView, CreateView, ListView
from .models import Character, Type, Item
from .forms import CharacterCreate, CreateMatch
from game.apps.match.models import Match, Enemy
from django.views.generic.edit import ModelFormMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from game.apps.match.helpers import calculate_player_damage, calculate_boss_damage, calculate_player_health,  calculate_boss_health, calculate_xp


class ShopItems(ListView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ShopItems, self).get_context_data(**kwargs)
        # Need to filter by Class(type)
        context['item_list'] = Item.objects.all()
        for item in context['item_list']:
            if  self.request.user >= item.level_required:
                pass
            else:
                context['insufficient'] = "Insufficient Level"
        return context


class CharacterLeaderboard(ListView):
    model = Character

    def get_context_data(self, **kwargs):
        context = super(CharacterLeaderboard, self).get_context_data(**kwargs)
        context['character_list'] = Character.objects.all().order_by('-xp')[:100]
        return context


class CharacterDetail(DetailView):
    model = Character


class CreateMatch(CreateView):
    model = Match
    form_class = CreateMatch

    def get_context_data(self, **kwargs):
        context = super(CreateMatch, self).get_context_data(**kwargs)
        character = get_object_or_404(
            Character,
            pk=self.kwargs.get('pk'),
            user=self.request.user
        )
        context['character'] = character

        context['enemys'] = Enemy.objects.all()
        return context

    def form_valid(self, form):
        Form = form.save(commit=False)
        boss = form.cleaned_data['enemy']
        Form.enemy_health = calculate_boss_health(boss)
        Form.resource = 1
        character = Character.objects.get(user=1)

        Form.character_health = calculate_player_health(character)
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)


class CharacterCreate(CreateView):
    model = Character
    form_class = CharacterCreate

    def form_valid(self, form):
        charactercreate = form.save(commit=False)
        charactercreate.user = self.request.user
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CharacterCreate, self).get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context

    def get_success_url(self):
        return reverse('character:detail', kwargs={'pk': self.object.pk})


#class DeleteCharacter(UpdateView):
#    model = Character
