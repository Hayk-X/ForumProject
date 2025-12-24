from django.shortcuts import render, redirect
from .models import Post, Profile, Comment
from .forms import UserRegister, CommentForm, PostForm
from django.contrib.auth import login
from django.utils import timezone
def main_page(request):
    posts = Post.objects.all()
    return render(request, "main_page.html",{"posts": posts})

def comment_view(request, id):
    post= Post.objects.get(id = id)
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

def profile_view(request):
    return render(request, "profile.html", {})



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