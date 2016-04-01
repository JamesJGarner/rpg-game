from django.views.generic import UpdateView
from django.views.generic.edit import ModelFormMixin
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User
from game.apps.characters.models import Character
from game.apps.matches.models import Match


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

        context['wins'] = Match.objects.filter(character=self.object.pk, enemy_health=0).count()
        context['loses'] = 10;
        context['percent_of_wins'] = "20%"
        context['most_used_spell'] = "Fire"
        context['total_damage_dealt'] = 500;
        context['total_damage_taken'] = 200;
        return context
