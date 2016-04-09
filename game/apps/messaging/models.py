from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    from_user = models.ForeignKey(
        User,
        related_name='from_user'
        )

    to_user = models.ForeignKey(
        User
        )

    content = models.TextField()

    date = models.DateTimeField()


    def unicode(self):
        return self.from_user