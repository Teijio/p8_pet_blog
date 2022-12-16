from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile

# сигналы нужно подключить в apps.py !

# функции сигналы
# создаст профайл при создании юзера
@receiver(post_save, sender=User)
def profile_created(sender, instance, created, **kwargs):
    print("Profile signal triggered!")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name  
        )

# при удаление профайла удалится и юзер
@receiver(post_delete, sender=Profile)
def profile_deleted(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# post_save.connect(profile_updated, sender=User)
# post_delete.connect(profile_updated, sender=Profile)