from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


class RedirectAuthenticationMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            redirect_to = reverse("admin:index")
            return HttpResponseRedirect(redirect_to)
        else:
            return super().dispatch(request, *args, **kwargs)
