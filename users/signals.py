from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

from django.db.models.signals import post_save, post_delete

from .models import Profile

# сигналы нужно подключить в apps.py !

# функции сигналы
# создаст профайл при создании юзера
@receiver(post_save, sender=User)
def profile_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        subject = "Welcome to Yatube"
        message = "GG WP ^^"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


# при удаление профайла удалится и юзер
@receiver(post_delete, sender=Profile)
def profile_deleted(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# post_save.connect(profile_updated, sender=User)
# post_delete.connect(profile_updated, sender=Profile)
