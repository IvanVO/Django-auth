from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save

from .models import Profile

"""
Django Signals helps allow decoupled applications get notified when actions occur elsewhere in the framework.

In the case of authetication signals help create a user's profile once the user has been created in the registration page.

Below a user will be added to
"""
# The user will be added to the Customer group by default when a new account is created.
def createUserProfile(sender, instance, created, **kwargs): # This is a reciver
    if created:
        group = Group.objects.get(name='Customer')
        instance.groups.add(group)

        Profile.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email
        )

        print("Profile succesffully created")

post_save.connect(createUserProfile, sender=User)
