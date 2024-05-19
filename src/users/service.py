"""User service."""
from typing import List, Union

from src.users.models import User


class UserService:
    """
    User service.
    """
    @staticmethod
    def get_user(email: str) -> Union[User, None]:
        """
        Get user.

        :param email: Email (str)
        :return: User or None
        """

        user = User.objects.get(email=email)
        if user:
            return user
        return None

    @staticmethod
    def create_user(email: str, password: str) -> User:
        """ Create a new user."""
        return User.objects.create_user(email, password)

    @staticmethod
    def get_active_users() -> List[User]:
        """ Get list with active user"""
        return User.objects.active()

    @staticmethod
    def update_user(user: User, email: str, full_name: str, phone: str, image: str) -> User:
        """
        Update user data.

        :param user: User object.
        :param email: User email(str).
        :param full_name: User full name(str).
        :param phone: User phone number(str).
        :param image: New image for user(str).
        :return: User.
        """
        names = full_name.split(' ')
        user.first_name = names[0]
        user.last_name = names[1]

        user.email = email
        user.phone = phone
        user.image = image

        user.save()
        return user

