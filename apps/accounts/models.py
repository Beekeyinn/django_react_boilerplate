from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import ExtraFieldsModelsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError("User must have an username.")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, ExtraFieldsModelsMixin):
    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )
    username = models.CharField(_('username'),
                                max_length=150,
                                help_text=_(
                                    'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                                validators=[username_validator],)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email}"

    @property
    def is_staff(self):
        return self.is_admin
