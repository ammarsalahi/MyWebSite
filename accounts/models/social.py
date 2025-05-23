from utils.general_model import GeneralModel
from django.db import models

class Social(GeneralModel):
    name=models.CharField(
        verbose_name="نام",
        max_length=100
    )
    link=models.URLField(
        verbose_name="لینک"
    )

    status=models.CharField(
        max_length=100,
        verbose_name="وضعیت",
        blank=True,
        null=True
    )
    class Meta:
        verbose_name="حساب اجتماعی"
        verbose_name_plural="حساب‌های اجتماعی"

    def __str__(self):
        return self.name    