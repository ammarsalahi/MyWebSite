from django_filters import FilterSet,CharFilter
from contents.models import Post,Project
from django.db.models import Q


class PostFilter(FilterSet):
    q=CharFilter(method='search_post')
    sort=CharFilter(method='sorting')
    cate=CharFilter(method='search_category',field_name='دسته‌بندی')

    class Meta:
        model=Post
        fields=('q','sort','cate','keywords')

    def search_post(self,queryset,name,value):
        return  queryset.filter(
            Q(title__icontains=value)|
            Q(header__icontains=value)|
            Q(text__icontains=value)|
            Q(category_name__icontains=value)
        )    
    def sorting(self,queryset,name,value):
        if value==True:
            return queryset.order_by('created_at')
        else:
            return queryset.order_by('-created_at')
    
    def search_category(self,queryset,name,value):
        return queryset.filter(
            category_name=value
        )
    
class ProjectFilter(FilterSet):
    q=CharFilter(method='search_project')
    sort=CharFilter(method='sorting')

    class Meta:
        model=Project
        fields=('q','sort')

    def search_post(self,queryset,name,value):
        return  queryset.filter(
            Q(title__icontains=value)|
            Q(text__icontains=value)
        )    
    def sorting(self,queryset,name,value):
        if value==True:
            return queryset.order_by('created_at')
        else:
            return queryset.order_by('-created_at')
      