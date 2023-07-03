from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreatePostForm
from .models import FollowedPerson, Like, Post

# Create your views here.


def home(request):
    user = request.user
    posts = Post.objects.filter(user_id=user.id).order_by("create_date")
    users = User.objects.exclude(id=user.id).order_by("-date_joined")
    context = {
        "posts": posts,
        "users": users,
    }
    return render(request, "post.html", context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    post_detail = Post.objects.filter(id=post.id)
    user_is_liked = Like.objects.filter(
        post_id=post.id, user=request.user
    ).exists()
    liked_count = 0
    liked_count = Like.objects.filter(post_id=post.id).count()
    context = {
        "post_detail": post_detail,
        "user_is_liked": user_is_liked,
        "liked_count": liked_count,
    }
    return render(request, "details.html", context)


def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect("blog:post")
    else:
        form = CreatePostForm()
    context = {"form": form}
    return render(request, "create.html", context)


def view_person(request, id):
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(user_id=user.id)
    user_is_following = FollowedPerson.objects.filter(
        person=user, user=request.user
    ).exists()
    context = {
        "posts": posts,
        "user_is_following": user_is_following,
        "user": user,
    }
    return render(request, "view_person.html", context)


def follow(request, person_id):
    person = get_object_or_404(User, id=person_id)
    FollowedPerson.objects.create(person=person, user=request.user)
    return redirect("blog:view-person", person.id)


def unfollow(request, person_id):
    person = get_object_or_404(User, id=person_id)
    FollowedPerson.objects.filter(person=person, user=request.user).delete()
    return redirect("blog:view-person", person.id)


def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.create(post_id=post.id, user=request.user)
    return redirect("blog:post-detail", post.id)


def unlike(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.filter(post_id=post.id, user=request.user).delete()
    return redirect("blog:post-detail", post.id)
