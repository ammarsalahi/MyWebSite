from utils.general_model import GeneralModel
from django.db import models

class Image(GeneralModel):
    img=models.ImageField(
        upload_to='projects/imgs/',
        verbose_name="تصویر"
    )
    state=models.CharField(
        max_length="to Add",
        verbose_name="وضعیت"
    )

    class Meta:
        verbose_name="تصویر"
        verbose_name_plural="تصاویر"

    def __str__(self):
        return "{}".format(self.id)    