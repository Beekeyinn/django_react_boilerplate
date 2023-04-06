from django.contrib import admin

from apps.user_settings.models import Theme, UserSettings

# Register your models here.
admin.site.register(UserSettings)
admin.site.register(Theme)
