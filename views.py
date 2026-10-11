import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from .models import Post, Comment
from .forms import PostForm, CommentForm, RegisterForm

logger = logging.getLogger(__name__)


def home(request):
    posts = cache.get('home_posts')

    if posts is None:
        posts = list(
            Post.objects.all().order_by('-published_date')
        )
        cache.set('home_posts', posts, 60)
        logger.info("Home posts loaded from database and cached.")
    else:
        logger.info("Home posts loaded from cache.")

    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.prefetch_related('comments'),
        id=id
    )

    comments = post.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            cache.delete('home_posts')

            logger.info("Comment added to post %s.", post.id)

            return redirect('post_detail', id=post.id)

    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            cache.delete('home_posts')

            logger.info("New blog post created.")

            return redirect('home')

    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {
        'form': form
    })


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            logger.info("New user registered: %s", user.username)

            return redirect('profile')

    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {
        'form': form
    })


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            logger.info("User logged in: %s", user.username)

            return redirect('profile')

    else:
        form = AuthenticationForm()

    return render(request, 'blog/login.html', {
        'form': form
    })


@login_required
def profile(request):
    logger.info("Profile viewed: %s", request.user.username)

    return render(request, 'blog/profile.html')


def user_logout(request):
    logger.info("User logged out: %s", request.user.username)

    logout(request)

    return redirect('login')