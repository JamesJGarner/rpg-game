from django.views.generic import UpdateView
from django.views.generic.edit import ModelFormMixin
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User
from game.apps.characters.models import Character

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
        return context
