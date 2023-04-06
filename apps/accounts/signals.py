from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models import User
from apps.user_settings.models import Theme, UserSettings


@receiver(post_save, sender=User)
def create_user_default_settings(instance, sender, created, *args, **kwargs):
    if created:
        try:
            theme = Theme.objects.get(theme="Light Mode")
        except Theme.DoesNotExist:
            theme = Theme.objects.create(theme="Light Mode")
            UserSettings.objects.create(user=instance, theme=theme)
        else:
            UserSettings.objects.create(user=instance, theme=theme)
