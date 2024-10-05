from rest_framework.viewsets import ModelViewSet
from accounts.models import UserAbout,Social,Cooperation
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


class UserViewset(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

# class UserSigninView(APIView):

class UserSigninView(TokenObtainPairView):
    serializer_class=UserTokenSerializer     
    
        
class UserAbountViewset(ModelViewSet):
    queryset=UserAbout.objects.all()
    serializer_class=UserAboutSerializer
    lookup_field='user__id'

class SocialViewset(ModelViewSet):
    queryset=Social.objects.all()
    serializer_class=SocialSerializer    


class UserAboutShowView(APIView):
    def get(self,request,format=None):
        try:
            user=User.objects.get(username='ammar')
            about=UserAbout.objects.get(user=user)
            return Response(
                data=UserAboutSerializer(instance=about).data,
                status=status.HTTP_200_OK
            )
        except (User.DoesNotExist,UserAbout.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

class CooperationViewset(ModelViewSet):
    queryset=Cooperation.objects.all()
    serializer_class=CooperationSerializer
    
