from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


def LEVELS():
    level = 1
    while True:
        yield (level, level*200)
        level += 1


class Class(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
    

class Character(models.Model):

    user = models.ForeignKey(
        User,
    )

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    for_class = models.ForeignKey(
        Class,
    )

    # This will get removed / ignored when you have armor
    health = models.PositiveIntegerField(
        default=100,
    )

    xp = models.PositiveIntegerField(
        "Current XP",
        default=0,
        blank=True,
    )

    is_deleted = models.BooleanField(
        default=False,
        )
    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def level_data(self):
        total_xp = self.xp

        for level in LEVELS():
            # Subtract the amount of XP required to leave this level from the
            # total XP. This will determine whether we're still on this level
            # or not.
            if total_xp - level[1] < 0:
                return {
                    'current_level': level[0],
                    'progress': total_xp,
                    'total_xp_required': level[1],
                    'xp_percentage': (float(total_xp) / level[1]) * 100
                }
            else:
                total_xp = total_xp - level[1]

        # If we haven't returned at this point, we're at max level.
        final_level = LEVELS[-1]
        if total_xp > final_level[1]:
            total_xp = final_level[1]

        return {
            'current_level': final_level[0],
            'progress': total_xp,
            'total_xp_required': final_level[1],
            'xp_percentage': (float(total_xp) / final_level[1]) * 100
        }

    @models.permalink
    def get_absolute_url(self):
            return ("character:detail", (), {
                "pk": self.pk
            })
