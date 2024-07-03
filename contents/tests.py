from django.test import TestCase
from rest_framework.test import APITestCase,APIRequestFactory,APIClient
from django.urls import reverse
from rest_framework import status
from contents.api.views import PostViewSet
from contents.models import Post

class TestHelloWorld(APITestCase):
    def test_hello(self):
        response=self.client.get('/contents/posts/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class TestPostView(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.post1 = Post.objects.create(title='Test Post 1',post_id='111')
        self.post2 = Post.objects.create(title='Test Post 2',post_id='222')


    def test_list_posts(self):
        view = PostViewSet.as_view({'get': 'list'})
        request = self.factory.get('/posts/')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)     

    def test_retrieve_posts(self):
        view=PostViewSet.as_view({'get':'retrieve'})     
        request=self.factory.get('/posts/{}/'.format(self.post1.post_id))
        response=view(request,post_id=self.post1.post_id)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_create_post(self):
        view=PostViewSet.as_view({'post':'create'})
        request=self.factory.post('/posts/',data={'title':'hello','post_id':'3333'},format='json')
        response=view(request)
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)    




# from django.test import TestCase, APIRequestFactory

# from rest_framework import status

# from rest_framework.test import force_authenticate

# from.views import PostViewSet

# from.models import Post

# from.serializers import PostSerializer


# class TestPostViewSet(TestCase):

#     def setUp(self):

#         self.factory = APIRequestFactory()

#         self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')

#         self.post1 = Post.objects.create(title='Test Post 1', content='This is a test post')

#         self.post2 = Post.objects.create(title='Test Post 2', content='This is another test post')


#     def test_list_posts(self):

#         view = PostViewSet.as_view({'get': 'list'})

#         request = self.factory.get('/posts/')

#         force_authenticate(request, user=self.user)

#         response = view(request)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         self.assertEqual(len(response.data), 2)


#     def test_retrieve_post(self):

#         view = PostViewSet.as_view({'get': 'etrieve'})

#         request = self.factory.get('/posts/{}/'.format(self.post1.post_id))

#         force_authenticate(request, user=self.user)

#         response = view(request, post_id=self.post1.post_id)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         self.assertEqual(response.data['title'], self.post1.title)


#     def test_create_post(self):

#         view = PostViewSet.as_view({'post': 'create'})

#         data = {'title': 'New Test Post', 'content': 'This is a new test post'}

#         request = self.factory.post('/posts/', data, format='json')

#         force_authenticate(request, user=self.user)

#         response = view(request)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         self.assertEqual(Post.objects.count(), 3)


#     def test_update_post(self):

#         view = PostViewSet.as_view({'patch': 'partial_update'})

#         data = {'title': 'Updated Test Post'}

#         request = self.factory.patch('/posts/{}/'.format(self.post1.post_id), data, format='json')

#         force_authenticate(request, user=self.user)

#         response = view(request, post_id=self.post1.post_id)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         self.assertEqual(Post.objects.get(post_id=self.post1.post_id).title, 'Updated Test Post')


#     def test_delete_post(self):

#         view = PostViewSet.as_view({'delete': 'destroy'})

#         request = self.factory.delete('/posts/{}/'.format(self.post1.post_id))

#         force_authenticate(request, user=self.user)

#         response = view(request, post_id=self.post1.post_id)

#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#         self.assertEqual(Post.objects.count(), 1)        