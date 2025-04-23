from utils.general_model import GeneralModel
from django.db import models

class TelegramChannel(GeneralModel):
    
    channel_id = models.CharField(
        max_length=200,
        verbose_name="آیدی کانال"
    )
    is_selected = models.BooleanField(
        default=False,
        verbose_name="انتخاب شده"
    )
    type_channel = models.CharField(
        choices=[
            ("post","پست"),
            ("project","پروژه")
        ],
        max_length=100,
        verbose_name="نوع کانال"
    )
    
    class Meta:
        verbose_name="تلگرام"
        verbose_name_plural="تلگرام ها"
    
    
