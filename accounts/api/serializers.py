from rest_framework import serializers
from accounts.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User 
        fields='__all__'
        
    def to_representation(self,instance):
        data = super(UserSerializer, self).to_representation(instance)
        data.pop('password')
        return data      

class SocialSerializer(serializers.ModelSerializer):

    class Meta:
        model=Social
        fields='__all__'

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields='__all__'
class UserAboutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=UserAbout
        fields='__all__'

    def to_representation(self,instance):
        data = super(UserAboutSerializer, self).to_representation(instance)
        data['socials']=SocialSerializer(instance=instance.socials.all(),many=True).data
        data['skills'] = SkillSerializer(instance=instance.skills.all(),many=True).data
        data['fullname']=instance.fullname
        data['user_img']=instance.user_img
        return data   

class  CooperationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cooperation
        fields="__all__"


class UserTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        if '@' in attrs.get('username'):
            attrs['username']=User.objects.get(email=attrs.get('username'))
        data = super().validate(attrs)
        user = self.user
        # data['is_otp'] = user.is_two_factor_auth
        data['username']=user.username
        return data   

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"
