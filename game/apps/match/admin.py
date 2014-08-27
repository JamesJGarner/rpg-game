from django.contrib import admin
from .models import Match, Attack, Spell


class AttackAdmin(admin.TabularInline):
    model = Attack


class MatchAdmin(admin.ModelAdmin):
    inlines = [AttackAdmin]

admin.site.register(Match, MatchAdmin)


class SpellAdmin(admin.ModelAdmin):
    pass

admin.site.register(Spell, SpellAdmin)
