from utils.general_model import GeneralModel
from django.db import models
from django.utils.crypto import get_random_string
from froala_editor.fields import FroalaField
from django.contrib.humanize.templatetags.humanize import naturaltime,naturalday

class Post(GeneralModel):
    post_id=models.CharField(
        verbose_name="شناسه",
        max_length=25,
        null=True,
        blank=True
    )

    title=models.CharField(
        verbose_name="عنوان",
        max_length=200
    )

    english_title = models.CharField(
        verbose_name="عنوان انگلیسی",
        max_length=200,
        blank=True,
        null=True
    )

    header=models.CharField(
        max_length=400,
        verbose_name="چکیده",
        null=True,
        blank=True
    )

    english_header=models.CharField(
        max_length=400,
        verbose_name="چکیده انگلیسی",
        null=True,
        blank=True
    )

    header_image=models.ImageField(
        upload_to="posts/headers/",
        verbose_name="تصویر"
    )
    text= FroalaField(
        verbose_name="متن",
        null=True,
        blank=True
    )
    
    english_text= FroalaField(
        verbose_name="متن انگلیسی",
        null=True,
        blank=True
    )

    creator=models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name="all_posts"
    )
    view_count=models.IntegerField(
        default=0,
        verbose_name='بازدید'
    )


    keywords=models.ManyToManyField(
        'contents.Keyword',
        related_name="posts",
        blank=True,
        verbose_name='کلمات کلیدی'
    )
    category=models.ForeignKey(
        'contents.Category',
        on_delete=models.DO_NOTHING,
        verbose_name="دسته‌بندی"
    )
    is_active=models.BooleanField(
        default=True,
        verbose_name="فعال بودن"
    )
    class Meta:
        verbose_name="پست"
        verbose_name_plural="پست‌ها"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.post_id is None:
            self.post_id=get_random_string(length=12,allowed_chars='0123456789')
        super(Post, self).save(*args, **kwargs)

    @property 
    def post_date(self):
        human_date=naturaltime(self.created_at)
        if '،' in human_date:
            result=human_date.split("،")
            return '{} پیش'.format(result[0])
        else:
            return human_date

    @property
    def reading_time(self):
        words_per_minute = 150
        num_words = len(self.text.split())
        reading_time_minutes = num_words / words_per_minute
        if reading_time_minutes < 1:
            return "خواندن زیر 1 دقیقه"
        elif reading_time_minutes == 1:
            return "خواندن 1 دقیقه"
        else:
            return f"خواندن {reading_time_minutes:.2f} دقیقه"
    