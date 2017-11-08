from __future__ import unicode_literals

from django.db import models
from myPayApp_admin.models import MyPayAppUser

# Create your models here.

class Transaction(models.Model):

    paying_user = models.ForeignKey(MyPayAppUser, blank=False,
                                    related_name="paying_user")
    transaction_amount = models.BigIntegerField("Amount Paid", blank=False,
                                           null=True)
    payee_user = models.ForeignKey(MyPayAppUser, blank=False,
                                   related_name="payee_user")
    transaction_date = models.DateTimeField("Date of Transaction",
                                            blank=False, null=True)