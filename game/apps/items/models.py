from django.db import models
from game.apps.characters.models import Character, Class

class Group(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
    )

    def __unicode__(self):
        return self.name


class Position(models.Model):

    name = models.CharField(
        max_length=200,
        unique=True,
        )

    def __unicode__(self):
        return self.name


class Item(models.Model):

    name = models.CharField(
        max_length=200,
        unique=True,
    )

    icon = models.ImageField(
        upload_to='icon',
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to='items',
        blank=True,
        null=True,
    )

    group = models.ForeignKey(
	    Group,
    )

    worth = models.DecimalField(
	    decimal_places=2,
        max_digits=100,
    )

    for_class = models.ForeignKey(
	    Class,
    )

    level_required = models.PositiveIntegerField(
    )

    damage = models.PositiveIntegerField(
        default=0,
        null=True,
    )

    healing = models.PositiveIntegerField(
        default=0,
        null=True,
    )

    armor = models.PositiveIntegerField(
        default=0,
        null=True,
    )

    position = models.ManyToManyField(
        'Position',
        default=None,
        )

    def __unicode__(self):
        return self.name


class ItemAcquired(models.Model):
    character = models.ForeignKey(
        Character
        )
    item = models.ForeignKey(
        Item,
    )

    equipped_to = models.ForeignKey(
        Position,
        null=True,
        blank=True,
        )

    class Meta:
        unique_together = (('item','equipped_to'),)


    def clean(self):

        # Checks to see if item is the same class as the character
        try:
            Item.objects.get(id=self.item.id, for_class=self.character.for_class)
        except:
            raise ValidationError('Your character is the wrong class for this item.')

        
        if self.equipped_to:
            # Check if character is high enough level
            if not self.character.level_data()['current_level'] >= self.item.level_required:
                raise ValidationError('You are not a high enough level to equip this item.')

            # Checks to see if item can be equipped in place requested
            try:
                item = Item.objects.get(id=self.item.id, position=self.equipped_to.id)
            except:
                raise ValidationError('This item cannot be equipped here.')
        
            # Check to see if item is equipped somewhere else.
            if ItemAcquired.objects.filter(character=self.character, item=self.item,  equipped_to__isnull=False).exclude(pk=self.pk):
                raise ValidationError('This item is already equipped somewhere else.')