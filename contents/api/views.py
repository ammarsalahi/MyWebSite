from .serializers import *
from contents.models import *
from rest_framework.viewsets import ModelViewSet
from django.utils.crypto import get_random_string


class PostViewSet(ModelViewSet):
    queryset=Post.objects.all().order_by('-created_at')
    serializer_class=PostSerializer
    lookup_field='post_id'

    # def create(self,request,*args,**kwargs):
    #     data=request.data
    #     data._mutable=True
    #     data['post_id']='{}-{}'.format(
    #         get_random_string(length=4,allowed_chars='0123456789'),
    #         get_random_string(length=4,allowed_chars='0123456789')
    #     )
    #     data._mutable=False
    #     return super().create(self,request,*args,**kwargs)