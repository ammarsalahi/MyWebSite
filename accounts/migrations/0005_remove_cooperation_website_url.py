# Generated by Django 4.2 on 2024-10-04 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_cooperation_phone_number_alter_cooperation_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cooperation",
            name="website_url",
        ),
    ]