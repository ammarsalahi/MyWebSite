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
    lookup_field='user__username'

    def create(self,request,*args,**kwargs):
        data=request.data
        about=UserAbout.objects.create(
            description=data.get("description"),
            skill=data.get("skill"),
            university_name=data.get("university_name"),
            university_web=data.get("university_site"),
            user=request.user
        )
        social_ids=data.get("socials")
        for soc in social_ids:
            try:
                soci=Social.objects.get(id=int(soc))
                about.socials.add(soci)
                soci.status="Added"
                soci.save()
            except Social.DoesNotExist:
                pass    
        about.save()
        return Response(status=status.HTTP_201_CREATED)    

    def update(self,request,*args,**kwargs):
        data=request.data
        
        about=self.get_object()
        about.description=data.get("description")
        about.skill=data.get("skill")
        about.university_name=data.get("university_name")
        about.university_web=data.get("university_site")
        
        about.socials.clear()
        social_ids=data.get('socials')
        for soc in social_ids:
            social=Social.objects.get(id=soc)
            about.socials.add(social)
            social.status="Added"
            social.save()
        about.save()
        return Response(status=status.HTTP_201_CREATED)

class SocialViewset(ModelViewSet):
    queryset=Social.objects.all()
    serializer_class=SocialSerializer    


# class UserAboutShowView(APIView):
#     def get(self,request,format=None):
#         try:
#             user=User.objects.get(username='ammar')
#             about=UserAbout.objects.get(user=user)
#             return Response(
#                 data=UserAboutSerializer(instance=about).data,
#                 status=status.HTTP_200_OK
#             )
#         except (User.DoesNotExist,UserAbout.DoesNotExist):
#             return Response(status=status.HTTP_404_NOT_FOUND)

class CooperationViewset(ModelViewSet):
    queryset=Cooperation.objects.all()
    serializer_class=CooperationSerializer
    
