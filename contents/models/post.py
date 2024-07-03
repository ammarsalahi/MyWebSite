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
        null=True,
        blank=True
    )
    comments=models.ManyToManyField(
        'contents.Comment',
        related_name='comments_post',
        blank=True
    )
    actions=models.ManyToManyField(
        'contents.Interaction',
        related_name='actions_post',
        blank=True
    )
    keywords=models.ManyToManyField(
        'contents.Keyword',
        related_name="keyword_posts",
        blank=True
    )

    def __str__(self):
        return self.title



    