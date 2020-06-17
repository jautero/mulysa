# Generated by Django 3.0.6 on 2020-06-16 12:07

from django.db import migrations
from django.conf import settings

from utils import referencenumber

def generate_missing_custominvoice_reference_numbers(apps, schema_editor):
    CustomInvoice = apps.get_model('users', 'CustomInvoice')
    for invoice in CustomInvoice.objects.all():
        if invoice.reference_number is None:
            invoice.reference_number = referencenumber.generate(settings.CUSTOM_INVOICE_REFERENCE_BASE + invoice.id)
            invoice.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_memberservice_self_subscribe'),
    ]

    operations = [
        migrations.RunPython(generate_missing_custominvoice_reference_numbers),
    ]
