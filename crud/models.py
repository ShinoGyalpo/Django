from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField( max_length=200)
    discription = models.TextField(default="Good")

    def __str__(self):
        return self.title
    
    
class Contacts(models.Model):
    name = models.CharField( max_length=200)
    email = models.EmailField()   

    def __str__(self):
        return self.name