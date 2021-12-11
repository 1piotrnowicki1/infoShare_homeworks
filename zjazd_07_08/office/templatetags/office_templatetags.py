from datetime import datetime, date

from django import template

register = template.Library()


@register.simple_tag
def my_temp_tag(invoice_client):
    return invoice_client.replace('Z', 'ZZZZ')


# @register.filter
# def row_styler(invoice_date):
#     today = datetime.date.today()
#     if invoice_date - today > 7:
#         return 'ok'
#     if invoice_date - date in range(3, 7):
#         return 'almost-due'
#     else:
#         return 'new'
#     return mark_safe(style)

@register.filter
def row_styler(invoice):
    payment_status = invoice.status
    payment_date = invoice.payment_date
    today = date.today()
    if payment_status == "zaplacone":
        return 'paid'
    elif (payment_date - today).days > 7:
        return 'due'
    elif 0 < (payment_date - today).days < 7:
        return 'pay-now'
    elif (payment_date - today).days < 1:
        return 'overdue'