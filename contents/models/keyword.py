from utils.general_model import GeneralModel
from django.db import models

class Keyword(GeneralModel):
    name=models.CharField(
        verbose_name="نام",
        max_length=200
    )
    class Meta:
        verbose_name="کلیدواژه"
        verbose_name_plural="کلیدواژه‌ها"

    def __str__(self):
        return self.name    