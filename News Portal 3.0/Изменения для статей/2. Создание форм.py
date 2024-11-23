from django import forms  
from .models import Post  

class ArticleForm(forms.ModelForm):  
    class Meta:  
        model = Post  
        fields = ['title', 'content'] 