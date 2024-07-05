from utils.general_model import GeneralModel
from django.db import models


class Post(GeneralModel):
    post_id=models.CharField(
        verbose_name="شناسه",
        unique=True,
        max_length=20
    )
    title=models.CharField(
        verbose_name="عنوان",
        max_length=300
    )
    text=models.TextField(
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
    comments=models.ManyToManyField(
        'contents.Comment',
        related_name='comments_post',
        blank=True,
        verbose_name='نظرات'
    )

    keywords=models.ManyToManyField(
        'contents.Keyword',
        related_name="keyword_posts",
        blank=True,
        verbose_name='کلمات کلیدی'
    )

    def __str__(self):
        return self.title



    