from django.urls import path  
from . import views  

urlpatterns = [  
    path('articles/', views.articles_list, name='articles_list'),  
    path('articles/create/', views.articles_create, name='articles_create'),  
    path('articles/<int:pk>/edit/', views.articles_edit, name='articles_edit'),  
    path('articles/<int:pk>/delete/', views.articles_delete, name='articles_delete'),  
]  