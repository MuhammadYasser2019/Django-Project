from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
# Create your models here.


def validate_phone_number(value):
    regex = "(201)[0-9]{9}"
    if not (re.search(regex, value)):
        raise ValidationError(_('رقم التليفون دا مش مظبوط خليه يبدأ ب 2 '), params={'value': value}, )


# Create your models here.
class User(models.Model):

    full_name = models.CharField(max_length=100, blank=False)

    username = models.CharField(max_length=100, blank=False)

    password = models.CharField(max_length=100, blank=False)

    phone_number = models.CharField(max_length=12, unique=True, validators=[validate_phone_number])

    longitude = models.FloatField(default=0.0)

    latitude = models.FloatField(default=0.0)

    address_text = models.CharField(max_length=250)

    rate = models.FloatField(default=0.0)

    craft = models.IntegerField(default=0)

    available_today = models.BooleanField(default=True)

    available_now = models.BooleanField(default=True)

    # True = client, False = ostafandy
    user_type = models.BooleanField(default=True)
