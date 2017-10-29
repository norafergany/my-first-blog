from django.contrib import admin
from .models import Post, Comment, Category
from django.contrib.auth.models import User

# Register your models here.



# TODO find out why import models doens't work

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
