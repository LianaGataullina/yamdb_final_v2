import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    if value > datetime.date.today().year:
        raise ValidationError(
            ('Год %(value)s больше текущего'),
            params={'value': value},
        )
