from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .user_manager import UserManager


def get_default_image():
    return 'users/photo/userimg.png'

class User(AbstractBaseUser):
    first_name = models.CharField(
        max_length=300,
        verbose_name="نام",
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=300,
        verbose_name="نام خانوادگی",
        null=True,
        blank=True

    )
    username = models.CharField(
        max_length=200,
        verbose_name="نام کاربری",
        unique=True
    )
    email = models.EmailField(
        verbose_name="ایمیل",
        unique=True
    )

    profile_image=models.ImageField(
        upload_to="users/photo/",
        verbose_name="تصویر پروفایل",
        default=get_default_image(),

    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name="مدیر است؟"
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="فعال است؟"
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name="اعتبارسنجی شده است؟"
    )

    is_otp = models.BooleanField(
        default=False,
        verbose_name="اعتبارسنجی دو مرحله‌ای است؟"
    )
    class Meta:
        verbose_name="کاربر"
        verbose_name_plural="کاربران"

    objects = UserManager()
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username
