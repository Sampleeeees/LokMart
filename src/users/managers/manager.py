"""User manager."""
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    User manager class.
    """

    def create_user(self, email: str, password: str = None, **extra_fields):
        """
        Create user.

        :param email: User email(str).
        :param password: User password(str).
        :return: User object.
        """
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        """
        Create superuser.

        :param email: User email(str).
        :param password: User password(str).
        :param extra_fields: Dictionary of extra fields(dict)
        :return: Superuser(User)
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email=email, password=password, **extra_fields)

