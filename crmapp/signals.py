from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer


# The cutomer_profile function is a signal handler that
# is triggered when a new user is created (e.g., during user registration).
# It checks if the user was just created, associates them with the 'customer'
# group, and creates a corresponding customer profile by linking the user
# and assigning their username as the customer's name. Finally, it prints
# a message indicating that the profile has been created.


def cutomer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(user=instance, name=instance.username)
        print('profile created')


post_save.connect(cutomer_profile, sender=User)
