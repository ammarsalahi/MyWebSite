from rest_framework import serializers
from contents.models import *






class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Keyword
        fields="__all__"  


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

        
class PostSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    # header_img_url=serializers.SerializerMethodField()

    class Meta:
        model=Post
        fields="__all__"
    
    def to_representation(self, instance):
        data = super(PostSerializer, self).to_representation(instance)
        data['keywords'] = KeywordSerializer(instance=instance.keywords.all(), many=True).data
        data['persian_date']=instance.post_date
        return data

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model=Technology
        field='__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields="__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"
    def to_representation(self,instance):
        data = super(ProjectSerializer, self).to_representation(instance)
        data['techonologies']=TechnologySerializer(instance=instance.techonologies.all(),many=True).data
        return data    