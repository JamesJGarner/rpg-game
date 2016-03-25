from django.db import models
from game.apps.characters.models import Character, Type

class Spell(models.Model):

    name = models.CharField(
        max_length=140,
        )
    type = models.ForeignKey(
        Type,
        null=True,
    )
    description = models.TextField(
        null=True,
        )

    damage = models.PositiveIntegerField(
        )

    level_required = models.PositiveIntegerField(
        null=True,
        )

    turn_cooldown = models.PositiveIntegerField(
        )

    def __unicode__(self):
        return self.name