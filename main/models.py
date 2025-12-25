from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return f"{self.creator.username}: {self.content[:20]}"

class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    creation_time = models.DateTimeField(auto_now_add=True)
