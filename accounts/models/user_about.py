from utils.general_model import GeneralModel
from django.db import models

class UserAbout(GeneralModel):
    user=models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name="کاربر"
    )
    description=models.TextField(
        verbose_name="توضیحات"
    )
    skill=models.CharField(
        verbose_name="مهارت",
        max_length=200
    )
    university_name=models.CharField(
        verbose_name="نام دانشگاه",
        max_length=300,
    )
    university_web=models.URLField(
        null=True,
        blank=True,
        verbose_name="آدرس دانشگاه"
    )
    socials=models.ManyToManyField(
        'accounts.Social',
        related_name='user_socials',
        verbose_name="حساب‌های اجتماعی",
        blank=True
    )

    class Meta:
        verbose_name="درباره کاربران"
        verbose_name_plural="درباره کاربران"

    @property
    def fullname(self):
        return '{} {}'.format(self.user.first_name,self.user.last_name)
    
    @property 
    def user_img(self):
        return self.user.profile_image.url 

