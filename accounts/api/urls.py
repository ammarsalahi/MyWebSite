from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path


router=DefaultRouter()

router.register('abouts',UserAbountViewset,basename='abouts')
# router.register('users',UserViewset,basename='users')
router.register('socials',SocialViewset,basename='socials')

urlpatterns=router.urls

urlpatterns+=[
    path('about/',UserAboutShowView.as_view())
]