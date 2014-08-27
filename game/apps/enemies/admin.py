from django.contrib import admin
from .models import Enemy


class EnemyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enemy, EnemyAdmin)
