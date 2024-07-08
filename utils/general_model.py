from django.db import models


class GeneralModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ به‌روز‌رسانی"
    )

    class Meta:
        abstract = True
