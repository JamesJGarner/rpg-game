from django.db import models


class Enemy(models.Model):
    name = models.CharField(
        max_length=150,
        )
    level = models.PositiveIntegerField(
        default=1
        )
    health = models.PositiveIntegerField(
        default=100
        )

    top = models.PositiveIntegerField(
        null=True,
        )
    left = models.PositiveIntegerField(
        null=True,
    )
    def __unicode__(self):
        return self.name
