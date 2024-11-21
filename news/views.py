from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import NewsPost
from .forms import NewsPostForm


def news_list(request):
    """ View to list all news posts. """
    if request.user.is_staff:
        news_posts = NewsPost.objects.all().order_by('-created_at')
    else:
        news_posts = NewsPost.objects.filter(
            status='approved').order_by('-created_at')

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

            # Set status to 'approved' for staff users and 'pending' for others
            if request.user.is_staff:
                news_post.status = 'approved'
            else:
                news_post.status = 'pending'

            news_post.save()
            return redirect('news_list')
    else:
        form = NewsPostForm()
    return render(
        request, 'news/news_form.html',
        {'form': form, 'form_title': 'Add News Post'})


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
    return render(
        request, 'news/news_form.html',
        {'form': form, 'form_title': 'Edit News Post'})


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_authenticated)
def delete_news_post(request, post_id):
    """ View to delete a news post. """
    news_post = get_object_or_404(NewsPost, id=post_id)

    # Only allow the author or staff users to delete the post
    if request.user == news_post.author or request.user.is_staff:
        news_post.delete()
        return redirect('news_list')
    else:
        return redirect('news_detail', post_id=news_post.id)
