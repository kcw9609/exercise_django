from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    content = models.TextField()
    #author 추후 작성
