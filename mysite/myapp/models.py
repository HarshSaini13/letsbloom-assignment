from django.db import models

# Create your models here.
class Library(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    author = models.CharField(max_length=100, default="Harsh")
    genre = models.CharField(max_length=50, default="Unknown")