from django.shortcuts import render, redirect
from .models import Post, Comment, Profile
from .forms import UserRegister, CommentForm, PostForm
from django.contrib.auth import login
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def main_page(request):
    posts = Post.objects.all()
    return render(request, "main_page.html",{"posts": posts})

def comment_view(request, id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post_id = id)

    if request.method == 'POST':
        content = CommentForm(request.POST)
        if content.is_valid():
            Comment.objects.create(
                creator=request.user,
                post=post,
                content=content.cleaned_data["comment"],
                creation_time=timezone.now()
            )
            return redirect("comment_section", id=id)
        
    else:
        content = CommentForm()
        
    return render(request, "comments.html", {"comments": comments,
                                             "post": post,
                                             "form":content})


def register_view(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("main_page")
    
    else:
        form = UserRegister()
        
    return render(request, "register.html", {"form":form})



@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "profile.html", {"profile": profile})

@login_required
def edit_profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, "edit_profile.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })

def post_cr_view(request):
    if request.method == 'POST':
        data = PostForm(request.POST)
        if data.is_valid():
            Post.objects.create(
                creator=request.user,
                content=data.cleaned_data["content"],
                creation_time=timezone.now(),
                title=data.cleaned_data["title"]
            )
            return redirect("main_page")

    else:
        data = PostForm()

    return render(request, "post_creation.html", {"form": data})



@login_required
def other_profile_view(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    profile, created = Profile.objects.get_or_create(user=other_user)
    can_edit = request.user == other_user
    return render(request, "other_profile.html", {
        "profile": profile,
        "can_edit": can_edit
    })