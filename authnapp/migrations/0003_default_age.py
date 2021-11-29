# Generated by Django 2.2.24 on 2021-11-28 18:58

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0002_user_model_extend"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 11, 30, 18, 58, 50, 254584, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
    ]
