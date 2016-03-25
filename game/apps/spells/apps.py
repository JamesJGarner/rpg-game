from django.apps import AppConfig
from .models import Spell

class SpellsConfig(AppConfig):
    name = 'spells'


admin.site.register(Spell)