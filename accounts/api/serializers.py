from rest_framework import serializers
from accounts.models import *


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

class UserAboutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=UserAbout
        fields='__all__'

    def to_representation(self,instance):
        data = super(UserAboutSerializer, self).to_representation(instance)
        data['socials']=SocialSerializer(instance=instance.socials.all(),many=True).data
        data['fullname']=instance.fullname
        data['user_img']=instance.user_img
        return data   

class  CooperationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cooperation
        fields="__all__"