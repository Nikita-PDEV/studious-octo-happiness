from django.shortcuts import render, get_object_or_404, redirect  
from .models import Post  
from .forms import ArticleForm  

# Список статей с пагинацией и фильтрацией  
def articles_list(request):  
    articles = Post.objects.filter(post_type=Post.ARTICLE).order_by('-created_at')  
    paginator = Paginator(articles, 10)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    return render(request, 'articles/articles_list.html', {'articles': page_obj})  

def articles_create(request):  
    if request.method == 'POST':  
        form = ArticleForm(request.POST)  
        if form.is_valid():  
            article = form.save(commit=False)  
            article.post_type = Post.ARTICLE  # Убедитесь, что это статья  
            article.save()  
            return redirect('articles_list')  
    else:  
        form = ArticleForm()  
    return render(request, 'articles/article_form.html', {'form': form})  

def articles_edit(request, pk):  
    article = get_object_or_404(Post, pk=pk)  
    if request.method == 'POST':  
        form = ArticleForm(request.POST, instance=article)  
        if form.is_valid():  
            form.save()  
            return redirect('article_detail', pk=article.pk)  
    else:  
        form = ArticleForm(instance=article)  
    return render(request, 'articles/article_form.html', {'form': form})  

def articles_delete(request, pk):  
    article = get_object_or_404(Post, pk=pk)  
    if request.method == 'POST':  
        article.delete()  
        return redirect('articles_list')  
    return render(request, 'articles/article_confirm_delete.html', {'article': article}) 