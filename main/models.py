from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField( User, on_delete = models.CASCADE)
    bio = models.CharField(max_length=1000, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)


    def __str__(self):
        return self.user.username




class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    creation_time = models.DateTimeField()

class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    creation_time = models.DateTimeField()
