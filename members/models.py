from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 

class UserProfile(models.Model):
    USER_PROFICIENCY_CHOICES = [
        ('begginer', 'Begginer'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250, blank=True)
    proficiency = models.CharField(max_length=20, choices=USER_PROFICIENCY_CHOICES, blank=True)
    profile_image = CloudinaryField('image', blank = True, null='True')

    def __str__(self):
        return self.user.username

        