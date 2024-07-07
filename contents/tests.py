from django.test import TestCase
from rest_framework.test import APIRequestFactory
from contents.models import *
from django.contrib.auth import get_user_model
from contents.api.views import *
from rest_framework import status

User=get_user_model()

class TestPostView(TestCase):

    def setUp(self):
        self.factory=APIRequestFactory()
        self.user=User.objects.create_superuser(username="test",email="test@ts.com",password="1234")
        self.post1=Post.objects.create(title="post1",post_id="1111",creator=self.user)
        self.post2=Post.objects.create(title="post2",post_id="1112",creator=self.user)
        self.post3=Post.objects.create(title="post3",post_id="11113",creator=self.user)
        self.post4=Post.objects.create(title="post22",post_id="11122",creator=self.user)
        self.post5=Post.objects.create(title="post11",post_id="111133",creator=self.user)
        # self.post6=Post.objects.create(title="post23",post_id="111222",creator=self.user)
        # self.post7=Post.objects.create(title="post21",post_id="11113342",creator=self.user)
        # self.post8=Post.objects.create(title="post234",post_id="11123313",creator=self.user)
        # self.post9=Post.objects.create(title="post14",post_id="11111224",creator=self.user)

    def test_list_posts(self):
        view=PostViewSet.as_view({'get':'list'})
        request=self.factory.get('/contents/posts/')
        response=view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_retrieve_post(self):
        view=PostViewSet.as_view({'get':'retrieve'})
        request=self.factory.get('/contents/posts/{}/'.format(self.post1.post_id))
        response=view(request,post_id=self.post1.post_id)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_limit_list(self):
        view=NewPostsListView.as_view()
        request=self.factory.get('/contents/list-posts/')
        response=view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    # def test_create_post(self):
    #     view=PostViewSet.as_view({'post':'create'})
    #     request=self.factory.post('/contents/posts/',data={'title':'222','post_id':'1223','creator':self.user.id},format='json')
    #     response=view(request)
    #     self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_update_post(self):
        view=PostViewSet.as_view({'patch':'partial_update'})
        request=self.factory.patch('/contents/posts/{}/'.format(self.post1.post_id),data={'title':'new title'},format='json')
        response=view(request,post_id=self.post1.post_id)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_delete_post(self):
        view=PostViewSet.as_view({'delete':'destroy'})
        request=self.factory.delete('/contents/posts/{}/'.format(self.post1.post_id))
        response=view(request,post_id=self.post1.post_id)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class CommentTestView(TestCase):
    def setUp(self):
        self.factory=APIRequestFactory()
        self.user=User.objects.create_superuser(username="test2",email="test2@ts.com",password="1234")
        self.comment1=Comment.objects.create(text="hello",email=self.user.email)
        self.comment2=Comment.objects.create(text="bye",email=self.user.email)

    def test_list_comment(self):
        view=CommentViewSet.as_view({'get':'list'})
        request=self.factory.get('/contents/comments/')
        response=view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_retrieve_comment(self):
        view=CommentViewSet.as_view({'get':'retrieve'})
        request=self.factory.get('/contents/comments/{}/'.format(self.comment1.id))
        response=view(request,pk=self.comment1.id)
        self.assertEqual(response.status_code,status.HTTP_200_OK)     
    def test_create_comment(self):
        view=CommentViewSet.as_view({'post':'create'})
        request=self.factory.post('/contents/comments/',data={'text':'hello','email':self.user.email},format='json')
        response=view(request)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_update_comment(self):
        view=CommentViewSet.as_view({'patch':'partial_update'})
        request=self.factory.patch('/content/comments/{}/'.format(self.comment1.id),data={'text':'hi'})
        response=view(request,pk=self.comment1.id)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_delete_comment(self):
        view=CommentViewSet.as_view({'delete':'destroy'})
        request=self.factory.delete('/contents/comments/{}'.format(self.comment1.id))
        response=view(request,pk=self.comment1.id)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)            

class KeywordTestView(TestCase):
    def setUp(self):
        self.factory=APIRequestFactory()
        self.key1=Keyword.objects.create(name="hello")
        self.key2=Keyword.objects.create(name="bye")

    def test_list(self):
        view=KeywordViewSet.as_view({'get':'list'})
        request=self.factory.get('/contents/keywords/')
        response=view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_retrieve(self):
        view=KeywordViewSet.as_view({'get':'retrieve'})
        request=self.factory.get('/contents/keywords/{}/'.format(self.key2.id))
        response=view(request,pk=self.key2.id)
        self.assertEqual(response.status_code,status.HTTP_200_OK)     

    def test_create(self):
        view=KeywordViewSet.as_view({'post':'create'})
        request=self.factory.post('/contents/keywords/',data={'name':'keuuu'},format='json')
        response=view(request)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_update(self):
        view=KeywordViewSet.as_view({'patch':'partial_update'})
        request=self.factory.patch('/content/keywords/{}/'.format(self.key2.id),data={'text':'hi'})
        response=view(request,pk=self.key2.id)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_delete(self):
        view=KeywordViewSet.as_view({'delete':'destroy'})
        request=self.factory.delete('/contents/keywords/{}'.format(self.key2.id))
        response=view(request,pk=self.key2.id)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT) 






