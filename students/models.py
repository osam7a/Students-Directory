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

class Student(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='static/students', blank=True, null=True)

    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=20)
    
    social_accounts = models.ManyToManyField(SocialAccount, blank=True)

    def __str__(self):
        return self.name