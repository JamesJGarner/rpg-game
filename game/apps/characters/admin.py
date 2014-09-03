from django.contrib import admin
from .models import Character, Type, Item, Group


class CharacterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Character, CharacterAdmin)


class TypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Type, TypeAdmin)

admin.site.register(Item)

admin.site.register(Group)
