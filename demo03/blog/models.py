from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tag(models.Model):
    """标签页-与文章是多对多关系"""
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Category(models.Model):
    """分类表-与文章是一对多关系"""
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Article(models.Model):
    """文章表"""
    title = models.CharField(max_length=30) # 标题
    body = models.TextField()   # 内容
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    # 分类
    tag = models.ManyToManyField(Tag)   # 标签
    create_time = models.DateTimeField(auto_now=True)    # 创建时间
    update_time = models.DateTimeField(auto_now_add=True)   # 更新时间
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 作者
    views = models.IntegerField(default=0)  # 浏览数

    def __str__(self):
        return self.title


class Ads(models.Model):
    """广告表"""
    pic = models.ImageField(upload_to='ads')
    desc = models.CharField(max_length=20)
    url = models.CharField(max_length=20)
