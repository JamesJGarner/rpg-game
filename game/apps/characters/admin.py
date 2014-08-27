from django.contrib import admin
from .models import Character, Type


class CharacterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Character, CharacterAdmin)


class TypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Type, TypeAdmin)
