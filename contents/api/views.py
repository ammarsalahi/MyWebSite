from .serializers import *
from contents.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.utils.crypto import get_random_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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

class ProjectViewset(ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    lookup_field='project_id'    

class TechnologyViewset(ModelViewSet):
    queryset=Technology.objects.all()
    serializer_class=TechnologySerializer

class ImageViewset(ModelViewSet):
    queryset=Image.objects.all()
    serializer_class=ImageSerializer

class HomeView(APIView):
    def get(self,request,format=None):
        post_serializer=PostSerializer(instance=Post.objects.all()[:8],many=True)
        project_serializer=ProjectSerializer(instance=Project.objects.all()[:8],many=True)
        return Response(
            data={'posts':post_serializer.data, 'projects':project_serializer.data,},
            status=status.HTTP_200_OK
        )
