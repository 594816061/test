from django.shortcuts import render, redirect, reverse
from .models import Topics, Options
from django.http import HttpResponseRedirect


# Create your views here.


def check(func):
    def inner(req, *args):
        # if req.COOKIES.get('username'):
        if req.session.get('username'):
            return func(req, *args)
        else:
            return redirect(reverse('vote:login'))
    return inner


@check
def index(req):
    topics = Topics.objects.all()
    return render(req, 'test/index.html', locals())


@check
def detail(req, id):
    topic = Topics.objects.get(pk=id)
    if req.method == 'GET':
        return render(req, 'test/detail.html', locals())
    elif req.method == "POST":
        id = req.POST.get('id')
        option = Options.objects.get(pk=id)
        option.time += 1
        option.save()
        # print(reverse("vote:result", args=(id,)))
        return redirect(reverse("vote:result", args=(id,)))


def result(req, id):
    topic = Options.objects.get(pk=id).topic
    return render(req, 'test/result.html', locals())


def login(req):
    if req.method == 'GET':
        return render(req, 'test/login.html')
    else:
        if req.POST.get('username'):
            # res = redirect(reverse('vote:index'))
            # res.set_cookie('username', req.POST.get('username'))
            # return res
            req.session['username'] = req.POST.get('username')
            return redirect(reverse('vote:index'))
