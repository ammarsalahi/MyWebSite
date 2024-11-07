from django_filters import FilterSet,CharFilter,ModelMultipleChoiceFilter
from contents.models import *
from django.db.models import Q


class PostFilter(FilterSet):
    q=CharFilter(method='search_post')
    # sort=CharFilter(method='sorting')
    keywords=ModelMultipleChoiceFilter(
        queryset=Keyword.objects.all()
    )
    class Meta:
        model=Post
        fields=('q','keywords')

    def search_post(self,queryset,name,value):
        try:
            category=Category.objects.get(name=value)
            return  queryset.filter(
                Q(title__icontains=value)|
                Q(header__icontains=value)|
                Q(text__icontains=value)|
                Q(category=category)
            )
        except Category.DoesNotExist:
            return  queryset.filter(
                Q(title__icontains=value)|
                Q(header__icontains=value)|
                Q(text__icontains=value)
            )    
    # def sorting(self,queryset,name,value):
    #     if value==1:
    #         return queryset.order_by('created_at')
    #     else:
    #         return queryset.order_by('-created_at')
    
    def search_category(self,queryset,name,value):
        return queryset.filter(
            category=Category.objects.get(name=value)
        )
    
class ProjectFilter(FilterSet):
    q=CharFilter(method='search_project')
    technologies =ModelMultipleChoiceFilter(
        queryset=Technology.objects.all(),
    )
    class Meta:
        model=Project
        fields=('q','technologies')

    def search_project(self,queryset,name,value):
        try:
            tech=Technology.objects.get(name=value)
            return  queryset.filter(
                Q(title__icontains=value)|
                Q(text__icontains=value)|
                Q(technologies=tech)
            ) 
        except Technology.DoesNotExist:
            return  queryset.filter(
                Q(title__icontains=value)|
                Q(text__icontains=value)
            )    
  