from  django.db.models.signals import post_save

from django.contrib.auth.models import User
from .models import Trainer
from django.contrib.auth.models import Group


def created_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="trainer")
        instance.groups.add(group)

        Trainer.objects.create(
            user=instance,
            name=instance.username,
            )
        print('Trainer profile created!')
        
post_save.connect(created_profile, sender=User)



        # Trainer.objects.create(user=instance)
        # print('Trainer profile created!')


def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.trainer.save()
        print('Trainer profile updated!')
        
post_save.connect(update_profile, sender=User)