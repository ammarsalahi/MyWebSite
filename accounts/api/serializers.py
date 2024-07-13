from rest_framework import serializers
from accounts.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        excludes=('password',)

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Social
        fields='__all__'

class UserAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAbout
        fields='__all__'