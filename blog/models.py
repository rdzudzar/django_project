from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #post model and user model will 
#have relationship, since users will author a post
from django.urls import reverse

# Create your models here.

#each class its going to be its table in the DB
class Post(models.Model): 
    #character field with max 100ch
    title = models.CharField(max_length=100) 
    content = models.TextField()
    #posted time
    date_posted = models.DateTimeField(default=timezone.now) 
    #del posts if usrer gets deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    #create how descriprion of the post looks like
    def __str__(self):
        return self.title
    
    #find location to a specific post; first to a route
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})