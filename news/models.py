from django.db import models
from tinymce.models import HTMLField

class News(models.Model):   
    news_title = models.CharField(max_length=100)
    news_description = HTMLField()
# Create your models here.
