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
from django.db.models import Q



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
        data={
            'posts':PostSerializer(instance=Post.objects.all().order_by('-created_at')[:8],many=True).data,
            'projects':ProjectSerializer(instance=Project.objects.all()[:8],many=True).data,
            # 'categories':CategorySerializer(instance=Category.objects.all(),many=True).data,
            # 'teches':TechnologySerializer(instance=Technology.objects.all(),many=True).data
        }
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

class FooterView(APIView):
    def get(self,request,format=None):
        data={
            'categories':CategorySerializer(instance=Category.objects.all(),many=True).data,
            'teches':TechnologySerializer(instance=Technology.objects.all(),many=True).data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    
class CategoryPostView(APIView):
    def get(self,request,name,format=None):
        try:
            cate=Category.objects.get(english_name=name)
            serializer=PostSerializer(instance=cate.post_set.all(),many=True)
            return Response(data=serializer.data)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class KeywordPostView(APIView):
    def get(self,request,name,format=None):
        try:
            keys=Keyword.objects.filter(english_name=name)
            serializer=PostSerializer(instance=Post.objects.filter(keywords__in=keys),many=True)
            return Response(data=serializer.data)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TechnologyProjectView(APIView):
    def get(self,request,name,format=None):
        try:
            teches=Technology.objects.filter(english_name=name)
            print(teches)
            serializer=ProjectSerializer(instance=Project.objects.filter(technologies__in=teches),many=True)
            return Response(data=serializer.data)
        except Technology.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class SearchView(APIView):
    def filterTwoModel(self,query:str)-> tuple:
        posts=Post.objects.filter(
            Q(title__icontains=query)|
            Q(header__icontains=query)|  
            Q(category__name__icontains=query)
        )
        keywords=Keyword.objects.filter(
            Q(name__icontains=query)|
            Q(english_name__icontains=query)
        )
        teches=Technology.objects.filter(
            Q(name__icontains=query)|
            Q(english_name__icontains=query)
        )
        projects=Project.objects.filter(
            Q(title__icontains=query)|
            Q(text__icontains=query)
        )
        keyword_posts = Post.objects.filter(keywords__in=keywords)
        teches_projects=Project.objects.filter(technologies__in=teches)
        postresult = posts | keyword_posts
        projectresult=projects|teches_projects

        return postresult,projectresult
    def create_post_json(self,obj):
        return {
            'types':'post',
            'post_id':obj.post_id,
            'title':obj.title,
            'header_image':obj.header_image.url,
            'category':{
                "name":obj.category.name
            },
            'persian_date':obj.post_date,
            'reading_time':obj.reading_time,
        }
    def create_project_json(self,obj):
        return {
            'types':'project',
            'project_id':obj.project_id,
            'title':obj.title,
            'header_image':obj.header_image.url,
            'persian_date':obj.project_date,
            'reading_time':obj.reading_time,
        }
    def get(self,request,format=None):
        q=request.GET.get('q')
        if q is not None:
            try:
                posts,projects=self.filterTwoModel(q)
                list_post=[self.create_post_json(obj) for obj in posts]
                list_project=[self.create_project_json(obj) for obj in projects]
                result=list_post+list_project
                return Response(data=result,status=status.HTTP_200_OK)
            except (Post.DoesNotExist,Project.DoesNotExist,Keyword.DoesNotExist,Technology.DoesNotExist):
                return Response(status=status.HTTP_404_NOT_FOUND)    
 


