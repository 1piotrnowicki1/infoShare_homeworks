from django.contrib import admin

# Register your models here.
from office.models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass