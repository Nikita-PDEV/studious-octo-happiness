from django.shortcuts import redirect  

def news_create(request):  
    if request.method == 'POST':  
        form = NewsForm(request.POST) 
        if form.is_valid():  
            form.save()  
            return redirect('news_list')  
    else:  
        form = NewsForm()  
    return render(request, 'news/news_form.html', {'form': form})  

def news_edit(request, pk):  
    post = get_object_or_404(Post, pk=pk)  
    if request.method == 'POST':  
        form = NewsForm(request.POST, instance=post)  
        if form.is_valid():  
            form.save()  
            return redirect('news_detail', pk=post.pk)  
    else:  
        form = NewsForm(instance=post)  
    return render(request, 'news/news_form.html', {'form': form})  

def news_delete(request, pk):  
    post = get_object_or_404(Post, pk=pk)  
    if request.method == 'POST':  
        post.delete()  
        return redirect('news_list')  
    return render(request, 'news/news_confirm_delete.html', {'post': post})  