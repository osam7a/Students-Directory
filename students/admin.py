from django.contrib import admin

from .models import Student, SocialAccount

# Register your models here.
admin.site.register(Student)
admin.site.register(SocialAccount)