from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import *


@receiver(post_save,sender=UserAbout)
def deleteToAddStatus(sender,instance,created,**kwargs):
    if created:
        socials=Social.objects.filter(status=f"TO ADD {sender.user.username}")
        for s in socials:
            s.delete()

@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )           
        

