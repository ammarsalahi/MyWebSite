from .serializers import *
from contents.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.utils.crypto import get_random_string


class PostViewSet(ModelViewSet):
    queryset=Post.objects.all().order_by('-created_at')
    serializer_class=PostSerializer
    lookup_field='post_id'

class NewPostsListView(ListAPIView):
    queryset=Post.objects.all()[:8]
    serializer_class=PostSerializer
    lookup_field="post_id"

    

class KeywordViewSet(ModelViewSet):
    queryset=Keyword.objects.all().order_by('-created_at')
    serializer_class=KeywordSerializer

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='name'