from django.db import models

SOCIAL_MEDIAS = (
    ('snapchat', 'Snapchat'),
    ('instagram', 'Instagram'),
    ('tiktok', 'TikTok'),
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
    ('linkedin', 'LinkedIn'),
    ('pinterest', 'Pinterest'),
)

# Create your models here.
class SocialAccount(models.Model):
    username = models.CharField(max_length=100)
    social_media = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.username

class Student:
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birthday = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    social_accounts = models.ManyToManyField(SocialAccount)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name