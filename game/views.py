from django.views.generic import ListView
from game.apps.characters.models import Character

class Homepage(ListView):
    model = Character
    template_name = 'site/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        context['characters'] = Character.objects.filter(user=self.request.user)
        return context
