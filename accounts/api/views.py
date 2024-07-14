from rest_framework.viewsets import ModelViewSet
from accounts.models import UserAbout,Social
from .serializers import *


class UserAbountViewset(ModelViewSet):
    queryset=UserAbout.objects.all()
    serializer_class=UserAboutSerializer
    lookup_field='user__id'

class SocialViewset(ModelViewSet):
    queryset=Social.objects.all()
    serializer_class=SocialSerializer    