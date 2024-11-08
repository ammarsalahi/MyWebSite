from utils.general_model import GeneralModel
from django.db import models


class Profile(GeneralModel):
    user=models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name="کاربر"
    )
    otp_code=models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    qrcode_image = models.ImageField(
        upload_to="users/qimages/",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name="پروفایل",
        verbose_name_plural="پروفایل‌ها"

    def __str__(self):
        return user.username    