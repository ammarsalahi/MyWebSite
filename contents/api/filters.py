from django_filters import FilterSet,CharFilter,ModelMultipleChoiceFilter
from contents.models import Post,Project,Technology,Keyword
from django.db.models import Q


class PostFilter(FilterSet):
    q=CharFilter(method='search_post')
    sort=CharFilter(method='sorting')
    cate=CharFilter(method='search_category',field_name='دسته‌بندی')
    keywords=ModelMultipleChoiceFilter(
        queryset=Keyword.objects.all()
    )
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
    technologies =ModelMultipleChoiceFilter(
        queryset=Technology.objects.all(),
    )
    class Meta:
        model=Project
        fields=('q','sort','technologies')

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
      