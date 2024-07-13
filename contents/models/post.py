from utils.general_model import GeneralModel
from django.db import models
from django.utils.crypto import get_random_string
from froala_editor.fields import FroalaField

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
    header_img=models.ImageField(
        upload_to="posts/headers/",
        verbose_name="تصویر"
    )
    text= FroalaField(
        verbose_name="متن",
        null=True,
        blank=True
    )
    

    creator=models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )
    view_count=models.IntegerField(
        default=0,
        verbose_name='بازدید'
    )


    keywords=models.ManyToManyField(
        'contents.Keyword',
        related_name="keyword_posts",
        blank=True,
        verbose_name='کلمات کلیدی'
    )
    categories=models.ForeignKey(
        'contents.Category',
        related_name="category",
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
            self.post_id=get_random_string(length=20,allowed_chars='0123456789')
        super(Post, self).save(*args, **kwargs)


    