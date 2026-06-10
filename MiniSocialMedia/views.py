from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Post, Like, Comment, Follow

# HOME
@login_required
def home(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'home.html', {'posts': posts})


# PROFILE
@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})
    

# CREATE POST
@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get('content')
        Post.objects.create(user=request.user, content=content)
    return redirect('home')


# LIKE / UNLIKE
@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)

    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()

    return redirect('home')


# COMMENT
@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        text = request.POST.get('text')
        Comment.objects.create(user=request.user, post=post, text=text)

    return redirect('home')


# DELETE COMMENT
@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if comment.user == request.user:
        comment.delete()

    return redirect('home')


# FOLLOW / UNFOLLOW
@login_required
def follow_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.user == user:
        return redirect('profile')

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=user
    )

    if not created:
        follow.delete()

    return redirect('profile')