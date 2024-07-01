from utils.general_model import GeneralModel
from django.db import models


class Interaction(GeneralModel):
    action=models.CharField(
        choices=(
            ('like','ثبت نام'),
            ('dislike', 'رمز عبور'),
        ),
        verbose_name="واکنش",
        max_length=100,
        null=True,
        blank=True
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