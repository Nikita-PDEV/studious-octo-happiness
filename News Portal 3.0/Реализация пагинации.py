from django.core.paginator import Paginator  
from django.db.models import Q  
from django_filters import rest_framework as filters  
from .models import Post  
from django.shortcuts import render  

# Поиск и фильтры  
class NewsFilter(filters.FilterSet):  
    title = filters.CharFilter(lookup_expr='icontains')  
    author = filters.CharFilter(field_name='author__username', lookup_expr='icontains')  
    created_at = filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))  

    class Meta:  
        model = Post  
        fields = ['title', 'author', 'created_at']  

def news_list(request):  
    news_filter = NewsFilter(request.GET, queryset=Post.objects.filter(post_type=Post.NEWS).order_by('-created_at'))  
    paginator = Paginator(news_filter.qs, 10) 

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    return render(request, 'news/news_list.html', {'news': page_obj, 'filter': news_filter})  