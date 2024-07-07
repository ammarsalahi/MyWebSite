from rest_framework import serializers
from contents.models import *




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"      


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Keyword
        fields="__all__"  

class PostSerializer(serializers.ModelSerializer):
    # keywords=KeywordSerializer()
    # comments=CommentSerializer()
    # actions=InteractionSerializer()
    
    class Meta:
        model=Post
        fields="__all__"
    def to_representation(self,instance):
        data = super(PostSerializer, self).to_representation(instance)
        return data