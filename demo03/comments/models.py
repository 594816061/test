from django.db import models
from blog.models import Article
# Create your models here.


class Comment(models.Model):
    """评论表"""
    name = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    email = models.EmailField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name