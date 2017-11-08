from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class MyPayAppUser(AbstractUser):

    USER_TYPE_CHOICE = (
        ("Normal","Normal"),
        ("Biller","Biller")
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICE,
        default="Normal"
    )
    objects = UserManager()

class BillerProfile(models.Model):

    BILL_TYPE_CHOICES = (
        ("Postpaid", "Postpaid"),
        ("Electricity", "Electricity"),
    )

    bill_type = models.CharField(
        max_length=20,
        choices=BILL_TYPE_CHOICES,
        default="Postpaid"
    )
    current_cash = models.BigIntegerField("Current Cash", null=False,
                                          blank=False, default=0)

class UserProfile(models.Model):

    current_cash = models.BigIntegerField("Current Cash", null=False,
                                          blank=False, default=0)