"""
标签工具模块
"""
from ..models import Article, Category, Tag, Ads
from django.template import Library

register = Library()


@register.simple_tag
def my_latest_articles(num=3):
    """按照时间获取文章的方法"""
    return Article.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def get_archive():
    """归档"""
    return Article.objects.all().dates('create_time', 'month')


@register.simple_tag
def get_category():
    """分类"""
    return Category.objects.all()


@register.simple_tag
def get_tag():
    """分类"""
    return Tag.objects.all()


@register.simple_tag
def get_ads():
    return Ads.objects.all()