
from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
       title= models.CharField(max_length=150)
       body = models.TextField()
       created = models.DateTimeField()
       author = models.CharField(max_length=30)
       tags = TaggableManager()


       def __unicode__(self):
           title = self.title

           return title

