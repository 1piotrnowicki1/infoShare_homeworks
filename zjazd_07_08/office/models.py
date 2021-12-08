from django.db import models

# Create your models here.
from accounts.models import ExtendedUser


class Invoice(models.Model):
    client = models.CharField('firma klienta', max_length=50, blank=True, null=True)
    payment_date = models.DateField('termin płatności')
    price = models.DecimalField('kwota faktury', decimal_places=2, max_digits=5, blank=True, null=True)
    status = models.CharField('status', max_length=50, blank=True)

