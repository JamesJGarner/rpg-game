from django.views.generic import UpdateView
from django.views.generic.edit import ModelFormMixin
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfilePage(UpdateView):
    model = UserProfile
    success_url = '/settings/'
    form_class = UserProfileForm
    template_name = 'userprofile/UserProfile_form.html'

   
    def get_object(self):
    	return User.objects.get(id=self.request.user.id)


    def form_valid(self, form):
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)
