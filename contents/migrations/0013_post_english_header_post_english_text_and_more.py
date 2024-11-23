# Generated by Django 4.2 on 2024-11-22 19:59

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ("contents", "0012_category_english_name_keyword_english_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="english_header",
            field=models.CharField(
                blank=True, max_length=400, null=True, verbose_name="چکیده انگلیسی"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="english_text",
            field=froala_editor.fields.FroalaField(
                blank=True, null=True, verbose_name="متن انگلیسی"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="english_title",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="عنوان انگلیسی"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="english_text",
            field=models.TextField(blank=True, null=True, verbose_name="متن انگلیسی"),
        ),
        migrations.AddField(
            model_name="project",
            name="english_title",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="عنوان انگلیسی"
            ),
        ),
    ]
