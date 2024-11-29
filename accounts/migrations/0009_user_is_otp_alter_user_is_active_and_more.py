# Generated by Django 4.2 on 2024-11-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_remove_profile_is_opt_profile_otp_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_otp",
            field=models.BooleanField(
                default=False, verbose_name="اعتبارسنجی دو مرحله\u200cای است؟"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="فعال است؟"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False, verbose_name="مدیر است؟"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_verified",
            field=models.BooleanField(
                default=False, verbose_name="اعتبارسنجی شده است؟"
            ),
        ),
    ]