from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from src.countries.models import Country
from src.users.managers.manager import UserManager
from src.users.managers.queryset import UserQuerySet


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    """
    Abstract base class implementing a fully featured User model.
    """

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="images/user/", blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(_("is active"), default=True)
    is_superuser = models.BooleanField(_("is superuser"), default=False)
    is_staff = models.BooleanField(_("is staff"), default=False)

    objects = UserManager.from_queryset(UserQuerySet)()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-date_created"]


class Address(models.Model):
    """Address model."""

    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=70)

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='addresses')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")

    def __str__(self):
        """Address string representation."""
        return self.address

