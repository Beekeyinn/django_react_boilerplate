"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from apps.accounts.views import (
    bad_request_error,
    page_not_found_error,
    permission_denied,
    server_error,
)
from apps.accounts.views.auth import LoginView
from base.utils import AuthenticatedRedirectView

api_url_patterns = []
accounts_url_patterns = [
    path(
        "accounts/password/change/",
        AuthenticatedRedirectView.as_view(pattern_name="account_login"),
    ),
    path(
        "accounts/password/set/",
        AuthenticatedRedirectView.as_view(pattern_name="account_login"),
    ),
    path(
        "accounts/inactive/",
        AuthenticatedRedirectView.as_view(pattern_name="account_login"),
    ),
    # E-mail
    path(
        "accounts/email/",
        AuthenticatedRedirectView.as_view(pattern_name="account_login"),
    ),
    path(
        "accounts/confirm-email/",
        AuthenticatedRedirectView.as_view(pattern_name="account_login"),
    ),
    re_path(
        r"^accounts/confirm-email/(?P<key>[-:\w]+)/$",
        AuthenticatedRedirectView.as_view(pattern_name="account_login"),
    ),
    # password reset
    path(
        "accounts/password/reset/",
        AuthenticatedRedirectView.as_view(pattern_name="account_login"),
    ),
    path(
        "accountspassword/reset/done/",
        AuthenticatedRedirectView.as_view(pattern_name="account_login"),
    ),
    re_path(
        r"^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        AuthenticatedRedirectView.as_view(pattern_name="account_login"),
    ),
    path(
        "accounts/password/reset/key/done/",
        AuthenticatedRedirectView.as_view(pattern_name="account_login"),
    ),
    path("accounts/", include("allauth.urls")),
]
urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", LoginView.as_view(), name="index"),
    ]
    + accounts_url_patterns
    + api_url_patterns
)
handler400 = bad_request_error
handler500 = server_error
handler403 = permission_denied
handler404 = page_not_found_error
