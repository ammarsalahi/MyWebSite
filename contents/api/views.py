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
        data['posts']=PostSerializer(instance=Post.objects.all()[:8],many=True).data
        data['projects']=ProjectSerializer(instance=Project.objects.all()[:8],many=True).data
        try:
            user=get_object_or_404(User,username="ammar")
            data['userimg']=request.build_absolute_uri(user.profile_image.url)
        except User.DoesNotExist:
            pass    
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
