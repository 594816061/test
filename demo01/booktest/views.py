from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import BookInfo, HeroInfo
from django.template import loader


# Create your views here.


def index(req):
    # return HttpResponse('这里是首页')
    # 获取模板
    # temp = loader.get_template('booktest/index.html')
    # # 使用模板渲染动态数据
    # res = temp.render({ '用户名':'WSH' })
    # # 返回渲染结果
    # return HttpResponse(res)
    return render(req, 'booktest/index.html', {'用户名': "WSH"})


def list(req):
    # books = BookInfo.objects.all()
    # temp = loader.get_template('booktest/list.html')
    # res = temp.render({ 'books':books })
    # return HttpResponse(res)
    return render(req, 'booktest/list.html', {'books': BookInfo.objects.all(), 'username': 'WSH'})


def detail(req, id):
    # book = BookInfo.objects.all().get(pk=id)
    #
    # temp = loader.get_template('booktest/detail.html')
    # res = temp.render({ 'book':book })
    #
    # return HttpResponse(res)
    return render(req, 'booktest/detail.html', {'book': BookInfo.objects.all().get(pk=id)})


def deletehero(req, id):
    """删除英雄"""
    hero = HeroInfo.objects.get(pk=id)
    hero.delete()
    return HttpResponseRedirect(f'/booktest/detail/{hero.book.id}')


def deletebook(req, id):
    """删除书籍"""
    book = BookInfo.objects.all().get(pk=id)
    book.delete()
    return HttpResponseRedirect('/booktest/list/')


def addhero(req, id):
    """添加英雄"""
    book = HeroInfo.objects.all().get(pk=id).book
    print(book)
    if req.method == 'GET':
        return render(req, 'booktest/addhero.html', {'id': id})
    elif req.method == 'POST':
        hero = HeroInfo()
        hero.name = req.POST.get('hero_name')
        hero.gender = req.POST.get('sex')
        hero.content = req.POST.get('hero_content')
        hero.book = book
        hero.save()
        return HttpResponseRedirect(f'/booktest/detail/{book.id}')
