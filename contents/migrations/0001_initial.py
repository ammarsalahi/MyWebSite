# Generated by Django 4.2 on 2024-07-13 18:08

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروز\u200cرسانی')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی\u200c',
                'verbose_name_plural': 'دسته\u200cبندی\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروز\u200cرسانی')),
                ('img', models.ImageField(upload_to='projects/imgs/', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروز\u200cرسانی')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'کلیدواژه',
                'verbose_name_plural': 'کلیدواژه\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروز\u200cرسانی')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'تکنولوژی',
                'verbose_name_plural': 'تکنولوژی\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروز\u200cرسانی')),
                ('project_id', models.CharField(max_length=12, verbose_name='شناسه')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('text', models.TextField(blank=True, null=True, verbose_name='متن')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('images', models.ManyToManyField(related_name='project_images', to='contents.image', verbose_name='تصاویر')),
                ('techonologies', models.ManyToManyField(related_name='project_technos', to='contents.technology', verbose_name='تکنولوژی\u200cها')),
            ],
            options={
                'verbose_name': 'پروژه',
                'verbose_name_plural': 'پروژه\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروز\u200cرسانی')),
                ('post_id', models.CharField(blank=True, max_length=25, null=True, verbose_name='شناسه')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('header_img', models.ImageField(upload_to='posts/headers/', verbose_name='تصویر')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='متن')),
                ('view_count', models.IntegerField(default=0, verbose_name='بازدید')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال بودن')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='contents.category', verbose_name='دسته\u200cبندی')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('keywords', models.ManyToManyField(blank=True, related_name='keyword_posts', to='contents.keyword', verbose_name='کلمات کلیدی')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست\u200cها',
            },
        ),
    ]
