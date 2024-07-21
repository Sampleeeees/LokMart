"""Help schemas module."""

from ninja import ModelSchema

from src.core.base_schema import BaseSchema
from src.helps.models import HelpCenter
from src.helps.models import WelcomeBlock


class WelcomeBlockModelSchema(ModelSchema):
    """Help model schema."""

    class Config(BaseSchema.Config):
        """Config class for welcome block."""

        model = WelcomeBlock
        model_fields = "__all__"


class HelpCenterModelSchema(ModelSchema):
    """Help center model schema."""

    class Config(BaseSchema.Config):
        """Config class for help center."""

        model = HelpCenter
        model_fields = "__all__"
