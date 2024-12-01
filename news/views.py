from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
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
                messages.info(request, "Your post is awaiting approval.")

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

    # Check if the user is the author or staff
    if request.user != news_post.author and not request.user.is_staff:
        return redirect('news_detail', post_id=news_post.id)

    if request.method == 'POST':
        form = NewsPostForm(request.POST, instance=news_post)
        if form.is_valid():
            news_post = form.save(commit=False)

            # Always set status to 'pending' for non-staff users after editing
            if not request.user.is_staff:
                news_post.status = 'pending'
                messages.info(
                    request, "Your edited post is awaiting approval.")

            news_post.save()
            return redirect('news_detail', post_id=news_post.id)
    else:
        form = NewsPostForm(instance=news_post)

    return render(
        request, 'news/news_form.html',
        {'form': form, 'form_title': 'Edit News Post'}
    )


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_authenticated)
def delete_news_post(request, post_id):
    news_post = get_object_or_404(NewsPost, id=post_id)

    # Check permissions
    if not (request.user == news_post.author or request.user.is_staff):
        return redirect('news_detail', post_id=news_post.id)

    if request.method == 'POST':
        news_post.delete()
        return redirect('news_list')

    return redirect('news_detail', post_id=post_id)


@login_required
@user_passes_test(lambda u: u.is_staff)
def approve_news_post(request, post_id):
    """ View for staff users to approve a pending news post. """
    news_post = get_object_or_404(NewsPost, id=post_id)

    # Approve the post
    if news_post.status == 'pending':
        news_post.status = 'approved'
        news_post.save()

    return redirect('news_list')
