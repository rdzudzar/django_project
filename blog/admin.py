from django.contrib import admin

# Register your models here.
from .models import Post

#to register posts on the admin site
admin.site.register(Post)