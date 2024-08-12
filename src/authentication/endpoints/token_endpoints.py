"""Token Obtain module."""

from django.http import HttpRequest
from ninja_extra import ControllerBase
from ninja_extra import api_controller
from ninja_extra import route
from ninja_extra.permissions import AllowAny
from ninja_jwt.schema_control import SchemaControl
from ninja_jwt.settings import api_settings

from src.core.base_openapi_extra import get_base_responses

schema = SchemaControl(api_settings)


@api_controller("/token", permissions=[AllowAny], tags=["auth"], auth=None)
class CustomTokenObtainPairController(ControllerBase):
    """Custom token obtain class."""

    @route.post(
        "/pair",
        response=get_base_responses(
            {
                200: schema.obtain_pair_schema.get_response_schema(),
            }
        ),
        url_name="token_obtain_pair",
    )
    def obtain_token(self, request: HttpRequest, user_token: schema.obtain_pair_schema) -> dict:
        """Get user's token.

        Params:
          - **request**: *HttpRequest* -> Request object.
          - **password**: *TokenInputSchemaMixin.password* -> User account password. ***(str)***
          - **email**: *TokenInputSchemaMixin.email* -> User email. ***(str)***

        Returns
        -------
          - **200**: *Success response* -> Authorize credentials.
          - **401**: *Error response* -> Unauthorized.
          - **500**: *Internal server response* -> Unexpected error.

        """
        user_token.check_user_authentication_rule()
        return user_token.to_response_schema()

    @route.post(
        "/refresh",
        response=get_base_responses(
            {200: schema.obtain_pair_refresh_schema.get_response_schema()},
        ),
        url_name="token_refresh",
    )
    def refresh_token(self, request: HttpRequest, refresh_token: schema.obtain_pair_refresh_schema) -> dict:
        """Refresh user token to new.

        Params:
          - **request**: *HttpRequest* -> Request object.
          - **refresh**: *TokenInputSchemaMixin.refresh* -> Refresh token. ***(str)***

        Returns
        -------
          - **200**: *Success response* -> Authorize credentials.
          - **401**: *Error response* -> Unauthorized.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return refresh_token.to_response_schema()

    @route.post(
        "/verify",
        response=get_base_responses({200: schema.verify_schema.get_response_schema()}),
        url_name="token_verify",
    )
    def verify_token(self, request: HttpRequest, token: schema.verify_schema) -> dict:
        """Check token is valid or not.

        Params:
          - **request**: *HttpRequest* -> Request object.
          - **token**: *TokenInputSchemaMixin.token* -> Token for verification. ***(str)***

        Returns
        -------
          - **200**: *Success response* -> Authorize credentials.
          - **401**: *Error response* -> Unauthorized.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return token.to_response_schema()
