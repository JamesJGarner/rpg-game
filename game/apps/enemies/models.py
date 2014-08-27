from django.db import models


class Enemy(models.Model):
    name = models.CharField(
        max_length=150,
        )
    level = models.PositiveIntegerField(
        max_length=16,
        default=1
        )
    health = models.PositiveIntegerField(
        max_length=16,
        default=100
        )

    def __unicode__(self):
        return self.name
