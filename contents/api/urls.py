from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path
router=DefaultRouter()

router.register('posts',PostViewSet,basename='posts')
router.register('comments',CommentViewSet,basename='comments')
router.register('keywords',KeywordViewSet,basename='keywords')


app_name="contents"

urlpatterns=router.urls

urlpatterns+=[
    path("list-posts/",NewPostsListView.as_view())
]