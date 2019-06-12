from django.shortcuts import render, redirect, reverse
from .models import Topics, Options, MyUser
from django.http import HttpResponseRedirect,HttpResponse
# from .forms import LoginForm
from .forms import MyUserLoginForm, MyUserRegistForm
from django.contrib import auth


# Create your views here.


def check(func):
    def inner(req, *args):
        # if req.COOKIES.get('username'):
        # print(req.session.get('username'))
        # print(req.user.is_authenticated)
        if req.user.username and req.user.is_authenticated:
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
        # lf = LoginForm()
        rf = MyUserRegistForm()
        lf = MyUserLoginForm()
        return render(req, 'test/login.html', locals())
    else:
        if req.POST.get('username'):
            # res = redirect(reverse('vote:index'))
            # res.set_cookie('username', req.POST.get('username'))
            # return res
            # req.session['username'] = req.POST.get('username')
            # lf = LoginForm(req.POST)
            # 判断表单是否有效
            # print(lf.is_valid())
            # username = lf.cleaned_data['username']
            username = req.POST.get('username')
            password = req.POST.get('password')
            user = auth.authenticate(req, username=username, password=password)
            if user:
                # 登录成功
                auth.login(req, user)
                return redirect(reverse('vote:index'))
            else:
                rf = MyUserRegistForm()
                lf = MyUserLoginForm()
                errormessage = '登录失败'
                return render(req, 'test/login.html', locals())


def regist(req):
    if req.method == "GET":
        pass
    else:
        # rf = MyUserRegistForm(req.POST)
        # rf.save()
        try:
            username = req.POST.get('username')
            password = req.POST.get('password')
            email = req.POST.get('email')
            user = MyUser.objects.create_user(username=username, password=password, email=email)
            if user:
                # 注册成功
                return redirect(reverse("vote:login"))
        except:
            rf = MyUserRegistForm()
            lf = MyUserLoginForm()
            errormessage = '注册失败'
            return render(req, 'test/login.html', locals())


def my_logout(req):
    auth.logout(req)
    rf = MyUserRegistForm()
    lf = MyUserLoginForm()
    return render(req, 'test/login.html', locals())

