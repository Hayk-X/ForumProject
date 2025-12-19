from django.shortcuts import render
from .models import Post, Profile, Comment

def main_page(request):
    posts = Post.objects.all()
    return render(request, "main_page.html",{"posts": posts})

def comment_view(request, id):
    post= Post.objects.get(id = id)
    comments = Comment.objects.filter(post_id = id)
    return render(request, "comments.html", {"comments": comments,
                                             "post": post})