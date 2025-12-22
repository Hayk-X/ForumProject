from django.shortcuts import render, redirect
from .models import Post, Profile, Comment
from .forms import UserRegister
from django.contrib.auth import login

def main_page(request):
    posts = Post.objects.all()
    return render(request, "main_page.html",{"posts": posts})

def comment_view(request, id):
    post= Post.objects.get(id = id)
    comments = Comment.objects.filter(post_id = id)
    return render(request, "comments.html", {"comments": comments,
                                             "post": post})


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

def profile_view(request):
    return render(request, "profile.html", {})