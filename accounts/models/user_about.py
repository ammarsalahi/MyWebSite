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
    english_description=models.TextField(
        verbose_name="توضیحات انگلیسی",
        blank=True,
        null=True
    )
    
    university_name=models.CharField(
        verbose_name="نام دانشگاه",
        max_length=300,
    )
    english_university_name=models.CharField(
        verbose_name="نام دانشگاه انگلیسی",
        max_length=300,
         blank=True,
        null=True
    )
    university_web=models.URLField(
        null=True,
        blank=True,
        verbose_name="آدرس دانشگاه"
    )
    skills = models.ManyToManyField(
        'accounts.Skill',
        related_name="skill_about",
        verbose_name="مهارت‌ها",
        blank=True
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

