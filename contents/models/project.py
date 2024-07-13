from utils.general_model import GeneralModel
from django.db import models

class Project(GeneralModel):
    project_id=models.CharField(
        verbose_name="شناسه",
        max_length=12
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
    def save(self, *args, **kwargs):
        if self.project_id is None:
            self.project_id=get_random_string(length=12,allowed_chars='0123456789')
        super(Project, self).save(*args, **kwargs)
    