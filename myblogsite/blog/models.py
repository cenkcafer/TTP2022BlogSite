from django.db import models

# Create your models here.

class Blog(models.Model):
    #create class and inherit from model class
    title = models.CharField(max_length=150)
    #creates a title for project, and how long it should be
    description = models.TextField()
    #creates a description for project, and how long it should be
    date = models.DateField()
    #creates a date for the project
    image = models.ImageField(upload_to='blog/images/', default=False)
    
    def __str__(self):
        return self.title