"""Module contains class for managing users data in the site."""

from django.utils.translation import gettext as _
from ninja.errors import HttpError

from src.users.models import User
from src.users.schemas import UserUpdateSchema


class UserService:
    """A service class for managing users."""

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        """Get user personal data by id.

        :param user_id: user id
        :return: User model instance
        """
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist as error:
            raise HttpError(404, _("Not Found: No User matches" " the given query.")) from error
        return user

    @staticmethod
    def update_my_profile(user_id: int, user_body: UserUpdateSchema) -> User:
        """Get user personal data by id.

        :param user_body: here fields that have to be updated
        :param user_id: user id
        :return: User model instance
        """
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist as error:
            raise HttpError(404, _("Not Found: No User matches" " the given query.")) from error
        if user_body.email:
            if User.objects.filter(email=user_body.email).exists():
                raise HttpError(400, _("User with this email already exists."))

        for key, value in user_body.dict().items():
            if value is not None:
                setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def get_my_profile(user_id: int) -> User:
        """Get user personal data by id.

        :param user_id: user id
        :return: User model instance
        """
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist as error:
            raise HttpError(404, _("Not Found: No User matches the given query.")) from error
