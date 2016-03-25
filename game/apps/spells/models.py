from django.db import models
from game.apps.characters.models import Character, _Class
from django.core.exceptions import ValidationError


class Spell(models.Model):

    name = models.CharField(
        max_length=140,
    )

    for_class = models.ForeignKey(
        _Class,
        null=True,
    )

    description = models.TextField(
        null=True,
    )

    damage = models.PositiveIntegerField()

    level_required = models.PositiveIntegerField(
        null=True,
    )

    turn_cooldown = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name


class SpellAcquired(models.Model):

    character = models.ForeignKey(
        Character
    )

    spell = models.ForeignKey(
        Spell
    )

    def __unicode__(self):
        return ', '.join([str(self.character), str(self.spell)])

    class Meta:
        unique_together = ('character', 'spell')
        verbose_name = "Acquired Spell"
        verbose_name_plural = "Acquired Spells"


    def clean(self):

        # Checks to see if item is the same class as the character
        try:
            Spell.objects.get(id=self.spell.id, for_class=self.character.for_class)
        except:
            raise ValidationError('Your character is the wrong class for this item.')
