class Post(models.Model):  
    NEWS = 'news'  
    ARTICLE = 'article'  
    POST_TYPE_CHOICES = [  
        (NEWS, 'News'),  
        (ARTICLE, 'Article'),  
    ]  

    title = models.CharField(max_length=200)  
    content = models.TextField()  
    post_type = models.CharField(max_length=7, choices=POST_TYPE_CHOICES)  
    created_at = models.DateTimeField(auto_now_add=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):  
        return self.title 