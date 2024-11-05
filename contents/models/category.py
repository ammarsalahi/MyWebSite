from utils.general_model import GeneralModel
from django.db import models
from contents.models import Post
class Category(GeneralModel):
    name=models.CharField(
        verbose_name="نام",
        max_length=200
    )

    class Meta:
        verbose_name="دسته‌بندی‌"
        verbose_name_plural="دسته‌بندی‌ها"

    def __str__(self):
        return self.name    

    @property 
    def post_count(self):
        try:
            return Post.objects.filter(category=self).count()
        except Post.DoesNotExist:
            return 0       