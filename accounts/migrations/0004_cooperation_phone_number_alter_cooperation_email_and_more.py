# Generated by Django 4.2 on 2024-07-20 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_cooperation_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperation',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='website_image',
            field=models.ImageField(blank=True, null=True, upload_to='cooperation/site_images/', verbose_name='نمونه تصویر'),
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='website_url',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس سایت مشابه'),
        ),
    ]
