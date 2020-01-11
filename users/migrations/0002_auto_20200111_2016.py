# Generated by Django 3.0.2 on 2020-01-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='reference_number',
            field=models.BigIntegerField(blank=True, help_text='Remember to always use your unique reference number for membership fee payments', null=True, verbose_name='Reference number of membership fee payments'),
        ),
    ]
