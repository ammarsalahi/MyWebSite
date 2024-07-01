from utils.general_model import GeneralModel
from django.db import models


class Comment(GeneralModel):
    text=models.CharField(
      verbose_name="متن",
      max_length=500
    )
    user=models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name="کاربر"
    )
    def __str__(self):
        return self.action

    class Meta:
        verbose_name="واکنش"
        verbose_name_plural="واکنش‌ها"