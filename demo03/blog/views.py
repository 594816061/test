from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View
from .models import *
from comments.models import *

# Create your views here.


class IndexView(View):
    """首页视图"""
    def get(self, req):
        articles = Article.objects.all()
        return render(req, 'blog/index.html', locals())


class SingleView(View):
    """详情页视图"""
    def get(self, req, id):
        """
        GET方法重写
        :param req: request，网页请求信息
        :param id: 跳转页面的文章id
        :return: 渲染相对应的详情页
        """
        article = get_object_or_404(Article, pk=id)
        return render(req, 'blog/single.html', locals())

    def post(self, req, id):
        """
        POST方法重写
        :param req: request，网页请求信息
        :param id: 评论文章的id
        :return: 重定向详情页
        """
        name = req.POST.get('name')
        email = req.POST.get('email')
        url = req.POST.get('url')
        content = req.POST.get('comment')
        comment = Comment()
        comment.article = get_object_or_404(Article, pk=id)
        comment.name = name
        comment.email = email
        comment.url = url
        comment.content = content
        comment.save()
        return redirect(reverse('blog:single', args=(id,)))