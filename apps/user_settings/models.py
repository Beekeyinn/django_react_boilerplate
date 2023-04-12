# Create your models here.
from django.db import models

from apps.accounts.models import User
from base.models import ExtraFieldsModelsMixin


# Create your models here.
class AllowedHostDomain(ExtraFieldsModelsMixin, models.Model):
    """
    Used to store all the domain name that can be logged in through google login.

    """

    host_domain = models.CharField(max_length=25)


class Theme(ExtraFieldsModelsMixin, models.Model):
    theme = models.CharField(unique=True, max_length=25)

    def __str__(self) -> str:
        return f"{self.theme}"


class UserSettings(ExtraFieldsModelsMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} -> {self.theme}"

    def change_theme(self):
        if self.theme.theme == "Dark Mode":
            self.theme = Theme.objects.get(theme="Light Mode")
        elif self.theme.theme == "Light Mode":
            self.theme = Theme.objects.get(theme="Dark Mode")
        else:
            self.theme = Theme.objects.get(theme="Light Mode")
        self.save()
