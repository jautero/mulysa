# Generated by Django 3.0.3 on 2020-03-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_auto_20200301_2012"),
    ]

    operations = [
        migrations.AddField(
            model_name="memberservice",
            name="hidden",
            field=models.BooleanField(
                default=False,
                help_text="True, if this service should not be shown for user member application form etc.",
            ),
        ),
    ]
