from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


User = settings.AUTH_USER_MODEL


# TODO: Create Deposit model.
# Deposits should be tied to a user, and should have an amount and timestamp.


# TODO: Create Withdrawal model.
# Withdrawals should be tied to a user, and should have an amount and timestamp.


# TODO: Create Interest model.
# Interests should be tied to a user, and should have an amount and timestamp.
