from utils.general_model import GeneralModel
from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.humanize.templatetags.humanize import naturaltime,naturalday

class Project(GeneralModel):

    project_id=models.CharField(
        verbose_name="شناسه",
        max_length=12,
        null=True,
        blank=True
    )
    title=models.CharField(
        verbose_name="عنوان",
        max_length=200
    )
    header_image=models.ImageField(
        upload_to='projects/imgs/',
        verbose_name="تصویر نمایه"
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
    technologies=models.ManyToManyField(
        'contents.Technology',
        related_name="projects",
        verbose_name="تکنولوژی‌ها"
    )
    is_active=models.BooleanField(
        default=False,
        verbose_name="قابل مشاهده"
    )
    class Meta:
        verbose_name="پروژه"
        verbose_name_plural="پروژه‌ها"

    def __str__(self):
        return self.project_id    

    def save(self, *args, **kwargs):
        print(self.project_id)
        if self.project_id is None:
            self.project_id=get_random_string(length=12,allowed_chars='0123456789')
        super(Project, self).save(*args, **kwargs)
    
    @property 
    def project_date(self):
        human_date=naturaltime(self.created_at)
        if '،' in human_date:
            result=human_date.split("،")
            return '{} پیش'.format(result[0])
        else:
            return human_date
    
    @property
    def reading_time(self):
        words_per_minute = 150
        num_words = len(self.text.split())
        reading_time_minutes = num_words / words_per_minute
        if reading_time_minutes < 1:
            return "خواندن زیر 1 دقیقه"
        elif reading_time_minutes == 1:
            return "خواندن 1 دقیقه"
        else:
            return f"خواندن {reading_time_minutes:.2f} دقیقه"    