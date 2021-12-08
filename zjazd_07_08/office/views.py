from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from office.models import Invoice


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['nazwa'] = 'Faktura1'
        return context
