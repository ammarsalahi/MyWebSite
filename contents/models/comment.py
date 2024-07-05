from utils.general_model import GeneralModel
from django.db import models


class Comment(GeneralModel):
    text=models.CharField(
      verbose_name="متن",
      max_length=500
    )
    email=models.EmailField(
        verbose_name="ایمیل"
    )
    is_verified=models.BooleanField(
        default=False,
        verbose_name="تایید شده"
    )
    def __str__(self):
        return self.action

    class Meta:
        verbose_name="واکنش"
        verbose_name_plural="واکنش‌ها"