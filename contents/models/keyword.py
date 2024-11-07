from utils.general_model import GeneralModel
from django.db import models

class Keyword(GeneralModel):
    name=models.CharField(
        verbose_name="نام",
        max_length=200
    )
    english_name=models.CharField(
        verbose_name="نام انگلیسی",
        max_length=200,
        blank=True,
        null=True
    )
    class Meta:
        verbose_name="کلیدواژه"
        verbose_name_plural="کلیدواژه‌ها"

    def __str__(self):
        return self.name    