from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.views.generic import View
from .models import *
from comments.models import *
from django.core.paginator import Paginator
from .tools import GetPage
import markdown
from django.core.mail import send_mail,EmailMultiAlternatives
from demo03 import settings
from django.views.decorators.cache import cache_page

# Create your views here.


class IndexView(View):
    """首页视图"""
    # @cache_page(60*5)
    def get(self, req):
        articles = Article.objects.all()
        newarticles = list()
        for article in articles:
            mk = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])
            article.body = mk.convert(article.body)
            article.toc = mk.toc
            newarticles.append(article)
        # print(articles)
        # paginator = Paginator(articles, 3)
        # num = req.GET.get('page')
        # num = 1 if num == 0 else num
        # page = paginator.get_page(num)
        # print(paginator.count)
        # print(paginator.object_list)
        # print(paginator.num_pages)
        # print(paginator.page_range)
        # print(page.paginator)
        p = GetPage()
        page = p.get_page(req, newarticles, 3)
        page.path = '/'
        return render(req, 'blog/index.html', {'page': page})


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
        mk = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        article.body = mk.convert(article.body)
        article.toc = mk.toc
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


class ArchiveView(View):
    def get(self, req, year, month):
        articles = Article.objects.filter(create_time__year=year, create_time__month=month)
        p = GetPage()
        page = p.get_page(req, articles, 1)
        page.path = f'/archive/{year}/{month}/'
        return render(req, 'blog/index.html', {'page': page})


class CategoryView(View):
    def get(self, req, id):
        articles = get_object_or_404(Category, pk=id).article_set.all()
        p = GetPage()
        page = p.get_page(req, articles, 1)
        page.path = f'/category/{id}/'
        return render(req, 'blog/index.html', {'page': page})


class TagView(View):
    def get(self, req, id):
        articles = get_object_or_404(Tag, pk=id).article_set.all()
        p = GetPage()
        page = p.get_page(req, articles, 1)
        page.path = f'/tag/{id}/'
        return render(req, 'blog/index.html', {'page': page})


class EmailView(View):
    def get(self, req):
        mail = EmailMultiAlternatives(subject="测试邮件html格式",
                                      body="<h1>  <a href = 'http://www.baidu.com'> 百度 </a>  </h1>",
                                      from_email=settings.DEFAULT_FROM_EMAIL,
                                      to=["594816061@qq.com", "WWW.2017.WSH.COM"])
        mail.content_subtype = "html"
        mail.send()

        return HttpResponse('发送成功')


