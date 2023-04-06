from rest_framework import serializers

from apps.user_settings.models import UserSettings


class UserSettingsSerializer(serializers.ModelSerializer):
    theme = serializers.StringRelatedField()

    class Meta:
        model = UserSettings
        fields = ("theme",)
