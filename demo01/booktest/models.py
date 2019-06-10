from django.db import models


# Create your models here.


# 继承models.Model可以拥有父类的功能~操作数据库
class BookInfo(models.Model):
    """图书类"""
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    """英雄类"""
    name = models.CharField(max_length=20)
    # gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    gender = models.CharField(max_length=5, choices=(('man', '男'), ('woman', '女')), null=True, blank=True)
    # book作为外键关联到表
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
