# Generated by Django 3.0.5 on 2020-05-07 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0017_auto_20200419_1901"),
    ]

    operations = [
        migrations.AddField(
            model_name="memberservice",
            name="self_subscribe",
            field=models.BooleanField(
                default=False,
                help_text="True, if this service can be subscribed and unsubscribed by users themselves.",
            ),
        ),
    ]
