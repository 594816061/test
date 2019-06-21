from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Pet(models.Model):
    """宠物表类"""
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=1)
    birthday = models.DateTimeField()
    intro = models.TextField()

    def __str__(self):
        return self.name


class Picture(models.Model):
    """宠物照片表类"""
    pic = models.ImageField(upload_to='pic')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


class Auth(User):
    """会员类"""
    pic = models.ImageField(upload_to='auth_pic')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username


class Blog(models.Model):
    """宠物博客表类"""
    title = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)
    auth = models.ForeignKey(Auth, on_delete=True)
    pic = models.ImageField(upload_to='blog_pic')
    mood = models.CharField(max_length=20)
    body = models.TextField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class About(models.Model):
    """关于"""
    pic = models.ImageField(upload_to='ab_pic')
    title = models.CharField(max_length=20)
    body = models.TextField()

    def __str__(self):
        return self.title


class SlideShow(models.Model):
    """轮播图类"""
    pic = models.ImageField(upload_to='slide_pic')
    slogan = models.CharField(max_length=50)


class Recommend(models.Model):
    """推荐类"""
    pic = models.ImageField(upload_to='recommend_pic')
    slogan = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)


class Welcome(models.Model):
    """欢迎类"""
    hint = models.CharField(max_length=100)
    body1 = models.TextField()
    body2 = models.TextField()
    pic1 = models.ImageField(upload_to='welcome_pic1')
    pic2 = models.ImageField(upload_to='welcome_pic2')


class HintTag(models.Model):
    """关于页面提示标签"""
    pic = models.ImageField(upload_to='hint_pic')
    hint = models.CharField(max_length=30)


class Comment(models.Model):
    """评论类"""
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=None)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)