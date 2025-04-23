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

    def to_representation(self,instance):
        data = super(CategorySerializer, self).to_representation(instance)
        data['post_count']=instance.post_count
        return data


        
class PostSerializer(serializers.ModelSerializer):
    category=CategorySerializer()

    class Meta:
        model=Post
        fields="__all__"
    
    def to_representation(self, instance):
        data = super(PostSerializer, self).to_representation(instance)
        data['keywords'] = KeywordSerializer(instance=instance.keywords.all(), many=True).data
        data['persian_date']=instance.post_date
        data['reading_time']=instance.reading_time
        return data

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model=Technology
        fields='__all__'

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
        data['technologies']=TechnologySerializer(instance=instance.technologies.all(),many=True).data
        data['images']=ImageSerializer(instance=instance.images.all(),many=True).data
        data['persian_date']=instance.project_date
        data['reading_time']=instance.reading_time

        return data    

class ChoiceContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChoiceContent
        fields="__all__"
    def to_representation(self,instance):
        data = super(ChoiceContentSerializer, self).to_representation(instance)
        data['selected_post'] = PostSerializer(instance=Post.objects.get(id=instance.get_post_id)).data
        return data

class TelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramChannel
        fields = "__all__"
    
