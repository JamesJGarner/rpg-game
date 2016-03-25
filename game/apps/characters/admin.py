from django.contrib import admin
from .models import Character, Class
from game.apps.items.models import ItemAcquired


class ItemAcquired(admin.TabularInline):
    model = ItemAcquired


class CharacterAdmin(admin.ModelAdmin):
    inlines = [ItemAcquired]


admin.site.register(Character, CharacterAdmin)
admin.site.register(Class)
