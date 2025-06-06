from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path


app_name="contents"


router=DefaultRouter()

router.register('posts',PostViewSet,basename='posts')
router.register('keywords',KeywordViewSet,basename='keywords')
router.register('categories',CategoryViewSet,basename='categories')
router.register('projects',ProjectViewset,basename="projects")
router.register('technologies',TechnologyViewset,basename='technologies')
router.register('images',ImageViewset,basename='images')
router.register("choices",ChoiceContentModelViewset,basename="choices")
router.register("telegrams",TelegramModelViewset,basename="telegrams")


urlpatterns=router.urls

urlpatterns+=[
    path('home/',HomeView.as_view()),
    path('post-detail/<str:id>/',PostFullDetailView.as_view()),
    path('project-detail/<str:id>/',ProjectFullDetailView.as_view()),
    path('new-posts/',newPostsView.as_view()),
    path('footer/',FooterView.as_view()),
    path('category-posts/<str:name>/',CategoryPostView.as_view()),
    path('keyword-posts/<str:name>/',KeywordPostView.as_view()),
    path('technology-projects/<str:name>/',TechnologyProjectView.as_view()),
    path('search/',SearchView.as_view()),
    path('keywords-add/',KeywordAddView.as_view()),
    path('technologies/add/',TechnologyAddView.as_view()),
    
    # path('posts-add/',AddPostView.as_view()),
]