from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

# TODO: Complete custom User model.
# The username field must be unique, and should include help text, validators, and error messages as appropriate.
# The email field and contact_no (phone number) field should be unique.
# Other portions of the application expect the following properties to be set:
# - account_no, returns the User's account number, if they have an account.
# - full_name, returns the User's full name, formatted as "first_name last_name".
# - balance, returns the User's account balance, if they have an account.
# - full_address, returns the User's full address, formatted as "street_address, city, state postal_code, country".
class User(AbstractUser):
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

    def __str__(self):
        return self.email


# TODO: Complete custom AccountDetails model.
# Accounts should have a one-to-one relationship with users.
# The account_no field must be unique.
class AccountDetails(models.Model):
    

    def __str__(self):
        return str(self.account_no)


# TODO: Complete custom UserAddress model.
# Addresses should be associated with users in a one-to-one relationship.
class UserAddress(models.Model):


    def __str__(self):
        return self.user.email
