from django.db import models
import watson
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(
        User
    )

    def __unicode__(self):
        return self.user.email

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
watson.register(UserProfile)


def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        up = UserProfile(user=user)
        up.save()
post_save.connect(create_profile, sender=User)

