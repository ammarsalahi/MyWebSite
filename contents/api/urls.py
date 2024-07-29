from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path
router=DefaultRouter()

router.register('posts',PostViewSet,basename='posts')
router.register('keywords',KeywordViewSet,basename='keywords')
router.register('categories',CategoryViewSet,basename='categories')
router.register('projects',ProjectViewset,basename="projects")
router.register('technologies',TechnologyViewset,basename='technologies')
router.register('images',ImageViewset,basename='images')



app_name="contents"

urlpatterns=router.urls

urlpatterns+=[
    path('home/',HomeView.as_view()),
    path('post-detail/<str:id>',PostFullDetailView.as_view()),
    path('project-detail/<str:id>',ProjectFullDetailView.as_view()),
    path('new-posts/',newPostsView.as_view()),
]