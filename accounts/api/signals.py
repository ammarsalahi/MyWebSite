from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Social,About


@receiver(post_save,sender=About)
def deleteToAddStatus(sender,instance,created,**kwargs):
    if created:
        socials=Social.objects.filter(status=f"TO ADD {sender.user.username}")
        for s in socials:
            s.delete()
            
