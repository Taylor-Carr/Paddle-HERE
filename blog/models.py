from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField 

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=150)
    body = models.TextField(max_length=800)
    post_image = CloudinaryField('image', blank = True, null=True)
    post_date = models.DateField(auto_now_add=True)
    country = models.CharField(default= 'England')
    category = models.CharField(default= 'Paddle Boarding')
    proficiency_level = models.CharField( default='beginner')
    tags = models.CharField(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    class Meta:
        ordering = ['-post_date'] 

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title + ' ¦ ' + str(self.author)

    
    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def total_comment_likes(self):
        return self.likes.count()
       

        