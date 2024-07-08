from utils.general_model import GeneralModel
from django.db import models
from django_quill.fields import QuillField

class Project(GeneralModel):
    project_id=models.CharField(
        verbose_name="شناسه",
        max_length=100
    )
    title=models.CharField(
        verbose_name="عنوان",
        max_length=200
    )
    images=models.ManyToManyField(
        'contents.Image',
        related_name='project_images',
        verbose_name="تصاویر"
    )
    text=models.TextField(
        verbose_name="متن",
        null=True,
        blank=True
    )
    creator=models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )
    techonologies=models.ManyToManyField(
        'contents.Technology',
        related_name="project_technos",
        verbose_name="تکنولوژی‌ها"
    )

    class Meta:
        verbose_name="پروژه"
        verbose_name_plural="پروژه‌ها"

    def __str__(self):
        return self.project_id    