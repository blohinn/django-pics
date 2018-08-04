from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Profile.objects.create(user=instance)
        Profile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)
    else:
        instance.profile.first_name = instance.first_name
        instance.profile.last_name = instance.last_name
        instance.profile.save()


@receiver(post_save, sender=Profile)
def update_user_model_from_profile(sender, instance, created, **kwargs):
    if not created:
        User.objects.filter(pk=instance.user.pk).update(
            first_name=instance.first_name,
            last_name=instance.last_name,
        )
