from django.db import models
from utils.general_model import GeneralModel

class Cooperation(GeneralModel):
	types=models.CharField(
		max_length=20,
		verbose_name="نوع پروژه"
	)
	name=models.CharField(
		max_length=300,
		verbose_name="نام کامل"
	)
	project_name=models.CharField(
		max_length=300,
		verbose_name="نام پروژه",
		null=True,
		blank=True
	)
	description=models.TextField(
		verbose_name="توضیحات",
		null=True,
		blank=True
	)

	website_image=models.ImageField(
		upload_to="cooperation/site_images/",
		verbose_name="نمونه تصویر",
		blank=True,
		null=True
	)
	email=models.EmailField(
		verbose_name="ایمیل",
		null=True,
		blank=True
	)
	phone_number=models.CharField(
		max_length=15,
		verbose_name="شماره موبایل",
		null=True,
		blank=True
	)

	class Meta:
		verbose_name="هماکاری"
		verbose_name_plural="همکاری ها"
	
