from django.db.models import Max
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import AccountDetails


# TODO: Create pre_save signal for AccountDetails that creates an account number if one does not exist.
