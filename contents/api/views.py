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
from .paginations import ContentPagination
from rest_framework.generics import GenericAPIView

User=get_user_model()

class PostViewSet(ModelViewSet):
    queryset=Post.objects.all().order_by('-created_at')
    serializer_class=PostSerializer
    lookup_field='post_id'
    filter_backends=[DjangoFilterBackend]
    filterset_class=PostFilter
    pagination_class=ContentPagination

    def create(self,request,*args,**kwargs):
        data=request.data
        cat_id=data.get('category')
        try:
            category=Category.objects.get(id=int(cat_id))
        except Category.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        img=request.FILES.get('header_image',None)    
        post = Post.objects.create(
            title=data.get('title'),
            text=data.get('text'),
            header=data.get('header'),
            header_image=img,
            creator=request.user,
            category=category,
            is_active=data.get('is_active')=='true'
        )         
        keys_id=data.getlist('keywords')
        for key in keys_id:
            try:
                keyword=Keyword.objects.get(id=int(key))
                post.keywords.add(keyword)
            except Keyword.DoesNotExist:
                pass
        post.save()
        return Response(status=status.HTTP_201_CREATED)        

    def update(self,request,*args,**kwargs):
        data=request.data
        cat_id=data.get('category')
        try:
            category=Category.objects.get(id=int(cat_id))
        except Category.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        img=request.FILES.get('header_image',None)   
        post=self.get_object()
        post.title=data.get('title')
        post.text=data.get('text')
        post.header=data.get('header')
        post.header_image=img
        post.category=category
        post.is_active=data.get('is_active')=='true'
              
        keys_id=data.getlist('keywords')
        for key in keys_id:
            try:
                keyword=Keyword.objects.get(id=int(key))
                post.keywords.add(keyword)
            except Keyword.DoesNotExist:
                pass
        post.save()
        return Response(status=status.HTTP_200_OK)


class KeywordViewSet(ModelViewSet):
    queryset=Keyword.objects.all().order_by('-created_at')
    serializer_class=KeywordSerializer

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class ProjectViewset(ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    lookup_field='project_id'   
    filter_backends=[DjangoFilterBackend]
    filterset_class=ProjectFilter 
    pagination_class=ContentPagination

    def create(self,request,*args,**kwargs):
        data=request.data
        img=request.FILES.get('header_image',None)    
        project=Project.objects.create(
            title=data.get("title"),
            header_image=img,
            text=data.get("text"),
            creator=request.user,
            is_active=data.get("is_active")=='true'
        )

        techs_id=data.getlist('teches')
        images_id=data.getlist('images')

        for tid in techs_id:
            try:
                tech=Technology.objects.get(id=tid)
                project.technologies.add(tech)
            except Technology.DoesNotExist:
                pass
        
        for imgid in images_id:
            try:
                img=Image.objects.get(id=imgid)
                project.images.add(img)
            except Image.DoesNotExist:
                pass

        project.save()
        return Response(status=status.HTTP_201_CREATED)

    def update(self,request,*args,**kwargs):
        data=request.data
        img=request.FILES.get('header_image',None)    
        project=self.get_object()
        project.title=data.get("title")
        project.header_image=img
        project.text=data.get("text")
        project.is_active=data.get("is_active")=='true'

        techs_id=data.getlist('teches')
        images_id=data.getlist('images')

        for tid in techs_id:
            try:
                tech=Technology.objects.get(id=tid)
                project.technologies.add(tech)
            except Technology.DoesNotExist:
                pass
        
        for imgid in images_id:
            try:
                img=Image.objects.get(id=imgid)
                project.images.add(img)
            except Image.DoesNotExist:
                pass

        project.save()
        return Response(status=status.HTTP_200_OK)



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


class CategoryPostView(GenericAPIView):
    pagination_class = ContentPagination
    serializer_class = PostSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        try:
            return Category.objects.get(english_name=name).post_set.all()
        except Category.DoesNotExist:
            return []
    def get(self, request, name, format=None):
        try:
            queryset = Category.objects.get(english_name=name).post_set.all()
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class KeywordPostView(GenericAPIView):
    pagination_class=ContentPagination
    serializer_class=PostSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        try:
            keywords=Keyword.objects.filter(english_name=name)
            return Post.objects.filter(keywords__in=keywords)
        except Keyword.DoesNotExist:
            return []
        
    def get(self,request,name,format=None):
        try:
            keywords=Keyword.objects.filter(english_name=name)
            queryset=Post.objects.filter(keywords__in=keywords)
            page=self.paginate_queryset(queryset)
            if page is not None:
                serializer=self.get_serializer(page,many=True)
                return self.get_paginated_response(serializer.data)
            serializer=self.get_serializer(page,many=True)
            return Response(serializer.data)
        except Keyword.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class TechnologyProjectView(GenericAPIView):
    pagination_class=ContentPagination
    serializer_class=ProjectSerializer
    def get_queryset(self):
        name = self.kwargs['name']
        try:
            teches=Technology.objects.filter(english_name=name)
            return Project.objects.filter(technologies__in=teches)
        except Technology.DoesNotExist:
            return []
        
    def get(self,request,name,format=None):
        try:
            teches=Technology.objects.filter(english_name=name)
            queryset=Project.objects.filter(technologies__in=teches)
            page=self.paginate_queryset(queryset)
            if page is not None:
                serializer=self.get_serializer(page,many=True)
                return self.get_paginated_response(serializer.data)
            serializer=self.get_serializer(page,many=True)
            return Response(serializer.data)
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
                final_result = self.paginate_queryset(result, request, view=self)
                return self.get_paginated_response(final_result)
            except (Post.DoesNotExist,Project.DoesNotExist,Keyword.DoesNotExist,Technology.DoesNotExist):
                return Response(status=status.HTTP_404_NOT_FOUND)    
 
class KeywordAddView(APIView):
    def post(self,request,format=None):
        name=request.data.get('name')
        try:
            key=Keyword.objects.get(name=name)
            return Response(
                data=KeywordSerializer(instance=key).data
            )
        except Keyword.DoesNotExist:
            key=Keyword.objects.create(
                name=name
            )  
            return Response(
                data=KeywordSerializer(instance=key).data
            )  

class TechnologyAddView(APIView):
    def post(self,request,format=None):
        name=request.data.get('name')
        try:
            tech=Technology.object.get(name=name)
            return Response(
                data=TechnologySerializer(instance=tech).data
            )
        except Technology.DoesNotExist:
            tech=Technology.objects.create(
                name=name
            )  
            return Response(
                data=TechnologySerializer(instance=tech).data
            )  
