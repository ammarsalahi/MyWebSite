from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path


router=DefaultRouter()

router.register('abouts',UserAbountViewset,basename='abouts')
router.register('users',UserViewset,basename='users')
router.register('socials',SocialViewset,basename='socials')
router.register('profiles',ProfileViewset,basename="profiles")
router.register('cooperations',CooperationViewset,basename="cooperations")
router.register('skills',SkillViewset,basename="skills")

urlpatterns=router.urls

urlpatterns+=[
    # path('about/',UserAboutShowView.as_view()),
    path('signin/',UserSigninView.as_view()),
    path('change-password/',UserPasswordChangeView.as_view()),
    path('verify-password/',UserPasswordVerify.as_view()),
    path("otp/",OtpGenerateView.as_view()),

]