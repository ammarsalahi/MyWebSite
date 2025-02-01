from utils.general_model import GeneralModel
from django.db import models


class ChoiceContent(GeneralModel):

    selected_post= models.ForeignKey(
        "contents.Post",
        on_delete=models.CASCADE,
        verbose_name="پست انتخاب شده"
    )
    priority = models.IntegerField(
        verbose_name="اولویت",
        default=0
    )

    class Meta:
        verbose_name="محتوای منتخب"
        verbose_name_plural="محتوای منتخب"

    def __str__(self)->str:
        return self.selected_post.title

    @property
    def get_post_id(self):
        return self.selected_post.id 
