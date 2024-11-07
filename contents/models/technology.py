from utils.general_model import GeneralModel
from django.db import models

class Technology(GeneralModel):
    name=models.CharField(
        max_length=200,
        verbose_name="نام"
    )
    english_name=models.CharField(
        verbose_name="نام انگلیسی",
        max_length=200,
        blank=True,
        null=True
    )
    class Meta:
        verbose_name="تکنولوژی"
        verbose_name_plural="تکنولوژی‌ها"

    def __str__(self):
        return self.name    