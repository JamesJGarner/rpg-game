from django.views.generic import DetailView, CreateView, ListView
from .models import Character, Type, Item
from .forms import CharacterCreate
from django.views.generic.edit import ModelFormMixin
from django.core.urlresolvers import reverse


class ShopItems(ListView):
    model = Item

    def get_context_data(self, **kwargs):
<<<<<<< HEAD
        context = super(ShopItems, self).get_context_data(**kwargs)
        # Need to filter by Class(type)
        context['item_list'] = Item.objects.all()
        for item in context['item_list']:
            if  self.request.user >= item.level_required:
                pass
            else:
                context['insufficient'] = "Insufficient Level"
        return context


=======
        context = super(ShopItmes, self).get_context_data(**kwargs)
        
        # Need to filter by Class(type)
        context['item_list'] = Item.objects.all()
        for item in context['item_list']:
            if  self.request.user >= item.required_level:
                pass
            else:
                context['insufficient'] = "Insufficient Level"
        return context 
        
    
    
>>>>>>> 91a17fa9f81ed82f73821b3d89e65eb9694a713b
class CharacterLeaderboard(ListView):
    model = Character

    def get_context_data(self, **kwargs):
        context = super(CharacterLeaderboard, self).get_context_data(**kwargs)
        context['character_list'] = Character.objects.all().order_by('-xp')[:100]
        return context

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
