# Generated by Django 4.2 on 2024-07-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_cooperation_alter_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperation',
            name='project_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='نام پروژه'),
        ),
    ]
