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
    lookup_field='username'

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
    
class UserPasswordChangeView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        data=request.data
        user=request.user
        if user.check_password(data['old_password']):
            user.set_password(data['new_password'])
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)    


class ProfileViewset(ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]
    lookup_field="user__username"
    
class OtpGenerateView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        user = request.user
        profile=Profile.objects.get(user=user)
        if profile.qrcode_image is None or profile.qrcode_image == '':
            secret = pyotp.random_base32()        
            profile.otp_code=secret
            profile.save()    
            totp = pyotp.TOTP(secret)
            qr_url = totp.provisioning_uri(user.email, issuer_name="BlogApp")
            qr_img = qrcode.make(qr_url)
            buffer = BytesIO()
            qr_img.save(buffer, format="PNG")
            buffer.seek(0)
            file_name = f'{user.username}_otp_qr.png' 
            profile.qrcode_image.save(file_name, File(buffer), save=True)
            serializer=ProfileSerializer(instance=profile)    
            return response.Response(data=serializer.data)
        # except Profile.DoesNotExist:
        #     return response.Response(status=status.HTTP_404_NOT_FOUND)

    def post(self,request,format=None):
        user = request.user
        otp = request.data.get('otp')
        
        secret = Profile.objects.get(user=user).otp_code
        totp = pyotp.TOTP(secret)
        
        if totp.verify(otp):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

