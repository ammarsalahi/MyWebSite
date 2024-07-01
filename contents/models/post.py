from utils.general_model import GeneralModel
from django.db import models


class Post(GeneralModel):
    title=models.CharField(
        verbose_name="عنوان",
        max_length=300
    )
    text=models.TextField(
        verbose_name="متن"
    )
    user=models.ForeignKey(
        'accounts.User',
        on_delete=models.CASECADE
    )
    comments=models.ManyToManyField(
        ''
    )

    