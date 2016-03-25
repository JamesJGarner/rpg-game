from django.contrib import admin
from .models import Match, Attack


class AttackAdmin(admin.TabularInline):
    model = Attack


class MatchAdmin(admin.ModelAdmin):
    inlines = [AttackAdmin]

admin.site.register(Match, MatchAdmin)


