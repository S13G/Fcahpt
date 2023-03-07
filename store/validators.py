from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    if not value.startswith('+'):
        raise ValidationError(_("Phone number must start with a plus sign (+)"))