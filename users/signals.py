
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings

# from django.dispatch import receiver
# @receiver(post_save, sender=Profile)

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name, 
        )

        subject = 'Welcome to DevSearch'
        message = "Thank you for signing up for our service. We're glad to have you!"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        # user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def profileDelete(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except User.DoesNotExist:
        print("User does not exist. This has to do with the relationship between User and Profile.")



post_save.connect(createProfile, sender=User)
post_delete.connect(profileDelete, sender=Profile)
post_save.connect(updateProfile, sender=Profile)
