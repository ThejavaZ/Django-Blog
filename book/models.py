from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    author = models.CharField(max_length=40, blank=True, null=True)
    release = models.DateField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, auto_created=True)
    
    def __str__(self):
        return self.name