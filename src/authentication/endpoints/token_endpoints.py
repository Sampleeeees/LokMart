"""
Token Obtain module.
"""
from django.http import HttpRequest
from ninja_extra import api_controller, ControllerBase, route
from ninja_extra.permissions import AllowAny
from ninja_jwt.schema_control import SchemaControl
from ninja_jwt.settings import api_settings


schema = SchemaControl(api_settings)


@api_controller("/token", permissions=[AllowAny], tags=["auth"], auth=None)
class CustomTokenObtainPairController(ControllerBase):
    """
    Custom token obtain class.
    """

    @route.post("/pair", response=schema.obtain_pair_schema.get_response_schema(), url_name="token_obtain_pair")
    def obtain_token(self, request: HttpRequest, user_token: schema.obtain_pair_schema) -> dict:
        """
        Get user's token

        :param request: HttpRequest
        :param user_token: Schema with user data for get token.

        :return:
        """
        user_token.check_user_authentication_rule()
        return user_token.to_response_schema()

    @route.post("/refresh", response=schema.obtain_pair_refresh_schema.get_response_schema(), url_name="token_refresh")
    def refresh_token(self, request: HttpRequest, refresh_token: schema.obtain_pair_refresh_schema) -> dict:
        """
        Refresh user token to new

        :param request: HttpRequest
        :param refresh_token: Schema with data for get new token

        :return:
        """

        return refresh_token.to_response_schema()

    @route.post("/verify", url_name="token_verify")
    def verify_token(self, request: HttpRequest, token: schema.verify_schema) -> dict:
        """
        Check token is valid or not

        :param request: HttpRequest
        :param token: Schema with token for checking
        :return:
        """
        return token.to_response_schema()
