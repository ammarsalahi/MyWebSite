from utils.general_model import GeneralModel
from django.db import models


class Skill(GeneralModel):

    name=models.CharField(
        verbose_name="نام",
        max_length=200
    )
    status=models.CharField(
        max_length=100,
        verbose_name="وضعیت",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name="مهارت"
        verbose_name_plural="مهارت ها"

        