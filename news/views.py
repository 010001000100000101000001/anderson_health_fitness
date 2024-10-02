from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import NewsPost
from .forms import NewsPostForm

def news_list(request):
    """ View to list all news posts. """
    news_posts = NewsPost.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news_posts': news_posts})

def news_detail(request, post_id):
    """ View to show a detailed view of a single news post. """
    news_post = get_object_or_404(NewsPost, id=post_id)
    return render(request, 'news/news_detail.html', {'news_post': news_post})

@login_required
def add_news_post(request):
    """ View to add a new news post. """
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            news_post = form.save(commit=False)
            news_post.author = request.user
            news_post.save()
            return redirect('news_list')
    else:
        form = NewsPostForm()
    return render(request, 'news/news_form.html', {'form': form})

@login_required
def edit_news_post(request, post_id):
    """ View to edit an existing news post. """
    news_post = get_object_or_404(NewsPost, id=post_id)
    if request.method == 'POST':
        form = NewsPostForm(request.POST, instance=news_post)
        if form.is_valid():
            form.save()
            return redirect('news_detail', post_id=news_post.id)
    else:
        form = NewsPostForm(instance=news_post)
    return render(request, 'news/news_form.html', {'form': form})
