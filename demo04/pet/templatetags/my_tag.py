from django.template import Library
from ..models import Blog, SlideShow, Recommend, About, Welcome, HintTag, Comment
from django.core.paginator import Paginator
from math import ceil

register = Library()


@register.simple_tag
def my_latest_blog(num=3):
    """按照时间顺序获得博客的方法"""
    return Blog.objects.all().order_by('-date')[:num]


@register.simple_tag
def my_slide_show():
    """轮播图标签"""
    return SlideShow.objects.all()[:3]


@register.simple_tag
def my_recommend_show():
    """推荐位标签"""
    return Recommend.objects.all()[:1]


@register.simple_tag
def my_about():
    """推荐位标签"""
    return About.objects.all()[:2]


@register.simple_tag
def my_welcome():
    """欢迎标签"""
    return Welcome.objects.all()[:1]


@register.simple_tag
def my_hint_tag():
    """提示标签"""
    return HintTag.objects.all()[:6]


@register.simple_tag
def my_comment_tag():
    """评论标签"""
    comments = Comment.objects.all()
    paginator = Paginator(comments, 2)
    page_num = ceil(comments.count() / 2)
    page = paginator.get_page(page_num)
    page.path = '/'
    return page


@register.simple_tag
def get_new_blog_tag():
    """提示标签"""
    return Blog.objects.all().order_by('-date')[:9]


@register.simple_tag
def get_new_comment_tag():
    """提示标签"""
    return Comment.objects.all().order_by('-date')[:3]