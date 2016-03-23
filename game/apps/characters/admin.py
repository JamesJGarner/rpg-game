from django.contrib import admin
from .models import Character, Type, Item, Group, CharacterItem, Position


class CharacterItem(admin.TabularInline):
    model = CharacterItem


class CharacterAdmin(admin.ModelAdmin):
    inlines = [CharacterItem]

admin.site.register(Character, CharacterAdmin)

admin.site.register(Type)

admin.site.register(Item)

admin.site.register(Group)

admin.site.register(Position)
