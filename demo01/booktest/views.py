from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo,HeroInfo
from django.template import loader
# Create your views here.


def index(req):
    # return HttpResponse('这里是首页')
    # 获取模板
    temp = loader.get_template('booktest/index.html')
    # 使用模板渲染动态数据
    res = temp.render({ '用户名':'WSH' })
    # 返回渲染结果
    return HttpResponse(res)


def list(req):

    books = BookInfo.objects.all()
    temp = loader.get_template('booktest/list.html')
    res = temp.render({ 'books':books })
    return HttpResponse(res)


def detail(req, id):
    book = BookInfo.objects.all().get(pk=id)

    temp = loader.get_template('booktest/detail.html')
    res = temp.render({ 'book':book })

    return HttpResponse(res)