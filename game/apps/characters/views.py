from django.views.generic import DetailView, CreateView, ListView
from .models import Character, Type
from .forms import CharacterCreate
from django.views.generic.edit import ModelFormMixin
from django.core.urlresolvers import reverse


class CharacterLeaderboard(ListView):
    model = Character


class CharacterDetail(DetailView):
    model = Character


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
