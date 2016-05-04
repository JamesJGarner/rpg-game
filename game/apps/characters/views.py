from django.views.generic import DetailView, CreateView, ListView
from .models import Character, Class
from .forms import CharacterCreate, CreateMatch
from game.apps.matches.models import Match, Enemy
from django.views.generic.edit import ModelFormMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from game.apps.matches.helpers import calculate_player_health, calculate_boss_health
from game.apps.spells.models import SpellAcquired
from game.apps.items.models import ItemAcquired, Position
from PIL import Image, ImageDraw, ImageOps
from random import randint
from django.http import HttpResponse


class CharacterLeaderboard(ListView):
    model = Character

    def get_context_data(self, **kwargs):
        context = super(CharacterLeaderboard, self).get_context_data(**kwargs)
        context['character_list'] = Character.objects.all().order_by('-xp')[:100]
        return context


class CharacterDetail(DetailView):
    model = Character


    def get_context_data(self, **kwargs):
        context = super(CharacterDetail, self).get_context_data(**kwargs)
        
        equipped_items =  ItemAcquired.objects.filter(character=self.object.pk, equipped_to__isnull=False)
        spells_acquired = SpellAcquired.objects.filter(character=self.object.pk)
        postions = Position.objects.all()
        context['spells'] = spells_acquired

        for i in postions:
            context[i.name.replace (" ", "_").lower()] = i

        for i in equipped_items:
            context["item_" + i.equipped_to.name.replace (" ", "_").lower()] = i.item.image.url
            context[i.equipped_to.name.replace (" ", "_").lower() + "_id"] = i.id


        return context


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
        character = Character.objects.get(pk=self.kwargs['pk'])
        Form.character = character
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
        context['types'] = Class.objects.all()
        return context

    def get_success_url(self):
        return reverse('character:detail', kwargs={'pk': self.object.pk})


def CharacterImage(request, pk):

    character =Character.objects.get(id=pk)
    media = "game/media/items/"
    background = Image.open("game/static/img/character-type/" + character.for_class.name + ".png")
    background = ImageOps.expand(background,border=80)

    equipped_items = ItemAcquired.objects.filter(character=pk, equipped_to__isnull=False)


    item_mapping = {
        'Head': (200, 27),
        'Left Hand': (55, 27),
    }

    hat = Image.open(media + "hat_nxY7RAW.png")
    background.paste(hat, (200, 27), hat)

    sword = Image.open(media + "sword-mounted_l9Rz3r8.png")
    background.paste(sword, (55, 27), sword)

    for i in equipped_items:
        item_image = Image.open("game" + i.item.image.url)
        background.paste(item_image, item_mapping[str(i.equipped_to)], item_image)

    response = HttpResponse(content_type="image/png")
    background.save(response, "PNG")


    return response

