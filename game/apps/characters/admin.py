from django.contrib import admin
from .models import Character, Type, Item, Group, Character_Items


class Character_Items(admin.TabularInline):
    model = Character_Items


class CharacterAdmin(admin.ModelAdmin):
    inlines = [Character_Items]

admin.site.register(Character, CharacterAdmin)


class TypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Type, TypeAdmin)

admin.site.register(Item)

admin.site.register(Group)
