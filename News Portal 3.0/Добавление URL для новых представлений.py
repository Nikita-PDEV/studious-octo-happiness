urlpatterns = [  
    path('news/', views.news_list, name='news_list'),  
    path('news/search/', views.news_search, name='news_search'),  
    path('news/create/', views.news_create, name='news_create'),  
    path('news/<int:pk>/edit/', views.news_edit, name='news_edit'),  
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),    
]  