from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('abouts',UserAbountViewset,basename='abouts')
router.register('socials',SocialViewset,basename='socials')

urlpatterns=router.urls