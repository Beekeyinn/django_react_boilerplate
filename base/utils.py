from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.views.generic import RedirectView



class AuthenticatedRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.pattern_name = settings.LOGIN_REDIRECT
        return super().get_redirect_url(*args, **kwargs)


# def get_user(request):
    
#     if settings.DEBUG and isinstance(request.user, AnonymousUser):
#         return User.objects.all().first()
#     else:
#         return request.user
