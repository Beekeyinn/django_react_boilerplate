from django.urls import path

from apps.user_settings.api.views import (
    UserSettingsApiView,
    UserSettingsChangeThemeApiView,
)

urlpatterns = [
    path("settings", UserSettingsApiView.as_view(), name="user_setting"),
    path("theme/change", UserSettingsChangeThemeApiView.as_view(), name="theme_change"),
]
