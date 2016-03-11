from django.db import models
from game.apps.enemies.models import Enemy
from game.apps.characters.models import Character, Type


class Match(models.Model):

    character = models.ForeignKey(
        Character,
        )

    enemy = models.ForeignKey(
        Enemy,
        )

    character_health = models.PositiveIntegerField(
        "Current Character Health",
        blank=True,
        )

    enemy_health = models.PositiveIntegerField(
        "Current Enemy Health",
        blank=True,
        )

    resource = models.PositiveIntegerField(
        default=1,
        )

    finished = models.BooleanField(
        default=False,
        )

    class Meta:
        verbose_name_plural = "Matches"

    def __unicode__(self):
        return self.character.name

    @models.permalink
    def get_absolute_url(self):
            return ("match:detail", (), {
                "pk": self.pk
            })


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


class Attack(models.Model):

    match = models.ForeignKey(
        Match
        )

    spell = models.ForeignKey(
        Spell
        )

    enemy_return_spell = models.ForeignKey(
        Spell,
        null=True,
        related_name='reliation'
        )

    damage_dealt = models.PositiveIntegerField(
        null=True,
        )

    damage_taken = models.PositiveIntegerField(
        null=True,
        )

    time = models.TimeField(
        null=True,
        )
