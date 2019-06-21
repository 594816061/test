from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMultiAlternatives
from demo04 import settings

# Create your views here.


def blog(req):
    if req.method == 'GET':
        blogs = Blog.objects.all()
        paginator = Paginator(blogs, 3)
        page_num = req.GET.get('page')
        page_num = 1 if page_num else page_num
        page = paginator.get_page(page_num)
        page.path = '/'

        return render(req, 'pet/blog.html', {'page': page})

    else:
        pass


def single(req, id):
    if req.method == 'GET':
        blog = Blog.objects.get(pk=id)
        return render(req, 'pet/single.html', {'blog': blog})


def index(req):
    if req.method == 'GET':
        return render(req, 'pet/index.html')


def about(req):
    if req.method == 'GET':
        return render(req, 'pet/about.html')


def care(req):
    if req.method == 'GET':
        return render(req, 'pet/404.html')


def picture(req):
    if req.method == 'GET':
        return render(req, 'pet/picture.html')


def contact(req):
    if req.method == 'GET':
        return render(req, 'pet/contact.html')


def comment(req, id):
    if req.method == 'POST':
        c = Comment()
        blog = Blog.objects.get(pk=id)
        c.blog = blog
        c.body = req.POST.get('comment')
        username = req.POST.get('username')
        c.auth = Auth.objects.get(username=username)
        c.save()
        return redirect(reverse('pet:single', args=(id,)))


def email(req):
    if req.method == 'POST':
        mail = EmailMultiAlternatives(subject="感谢您的反馈",
                                      body="<h1>  <a href = 'http://www.baidu.com'> 百度 </a>  </h1>",
                                      from_email=settings.DEFAULT_FROM_EMAIL,
                                      to=[req.POST.get('email')])
        mail.content_subtype = "html"
        mail.send()

        return redirect(reverse('pet:skip'))


def skip(req):
    return render(req, 'pet/skip.html')