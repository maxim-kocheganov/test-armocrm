from django.db import models

# Create your models here.

class Tag(models.Model):
    text = models.CharField(max_length=150)

class Post(models.Model):
    source = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    