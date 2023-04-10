from allauth.account.adapter import DefaultAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import render

from apps.user_settings.models import AllowedHostDomain


class OrganizationSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Organization based adapter.
    """

    def pre_social_login(self, request, sociallogin):
        """
        used to check if the domain of the email of social login is of some specified organization or not.
        """
        domain_lists = AllowedHostDomain.objects.values_list("host_domain")
        if not (request.GET.get("hd", "gmail.com"),) in domain_lists:
            response = render(request, "socialaccount/authentication_error.html")
            raise ImmediateHttpResponse(response)
        else:
            return super().pre_social_login(request, sociallogin)


class CustomAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return False
