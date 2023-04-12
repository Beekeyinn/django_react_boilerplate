from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user_settings.api.serializers import UserSettingsSerializer
from apps.user_settings.models import UserSettings
from base.decorator import exception_handler
from base.utils import get_user


class UserSettingsApiView(GenericAPIView):
    serializer_class = UserSettingsSerializer
    # permission_classes = [IsAuthenticated]

    @exception_handler
    def get(self, request, *args, **kwargs):
        user = get_user(request)
        user_settings = UserSettings.objects.get(user=user)
        serializer = self.serializer_class(user_settings)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserSettingsChangeThemeApiView(GenericAPIView):
    serializer_class = UserSettingsSerializer

    @exception_handler
    def get(self, request, *args, **kwargs):
        user = get_user(request)
        user_settings = UserSettings.objects.get(user=user)
        user_settings.change_theme()
        serializer = self.serializer_class(user_settings)
        return Response(serializer.data, status=status.HTTP_200_OK)
