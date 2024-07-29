from .serializers import *
from contents.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.utils.crypto import get_random_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User=get_user_model()

class PostViewSet(ModelViewSet):
    queryset=Post.objects.all().order_by('-created_at')
    serializer_class=PostSerializer
    lookup_field='post_id'
    filter_backends=[DjangoFilterBackend]
    filterset_class=PostFilter



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
    filter_backends=[DjangoFilterBackend]
    filterset_class=ProjectFilter 

class TechnologyViewset(ModelViewSet):
    queryset=Technology.objects.all()
    serializer_class=TechnologySerializer

class ImageViewset(ModelViewSet):
    queryset=Image.objects.all()
    serializer_class=ImageSerializer

class HomeView(APIView):
    def get(self,request,format=None):
        data={}
        data['posts']=PostSerializer(instance=Post.objects.all().order_by('-created_at')[:8],many=True).data
        data['projects']=ProjectSerializer(instance=Project.objects.all()[:8],many=True).data
        data['categories']=CategorySerializer(instance=Category.objects.all(),many=True).data
        data['teches']=TechnologySerializer(instance=Technology.objects.all(),many=True).data
        try:
            user=get_object_or_404(User,username="ammar")
            data['userimg']=request.build_absolute_uri(user.profile_image.url)
        except User.DoesNotExist:
            pass    
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )


class PostFullDetailView(APIView):
    def get(self,request,id,format=None):
        try:
            post=get_object_or_404(Post,post_id=id)
            data={
                'posts':PostSerializer(instance=post).data,
                'others':PostSerializer(instance=post.category.post_set.all(),many=True).data
            }
            return Response(data=data,status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProjectFullDetailView(APIView):
    def get(self,request,id,format=None):
        try:
            project=get_object_or_404(Project,project_id=id)
            data={
                'projects':ProjectSerializer(instance=project).data,
                'others':ProjectSerializer(instance=Project.objects.all(),many=True).data,
               
            }
            return Response(data=data,status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)        

class newPostsView(ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

