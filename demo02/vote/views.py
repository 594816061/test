from django.shortcuts import render, redirect, reverse
from .models import Topics, Options, MyUser
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
# from .forms import LoginForm
from .forms import MyUserLoginForm, MyUserRegistForm
from django.contrib import auth
from django.core.mail import send_mail,EmailMultiAlternatives
from demo02 import settings
from itsdangerous import TimedJSONWebSignatureSerializer
from PIL import Image, ImageDraw, ImageFont
import random,io
from django.core.cache import cache


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
            verifycode = req.POST.get('verifycode')
            # id = req.POST.get('id')
            user = auth.authenticate(req, username=username, password=password)
            if user:
                # 登录成功
                if verifycode == req.session["verifycode"]:     # cache.get('verifycode')
                    auth.login(req, user)
                    return redirect(reverse('vote:index'))
                else:
                    errormessage = '验证码输入错误'
                    return render(req, 'test/login.html', locals())

            else:
                rf = MyUserRegistForm()
                lf = MyUserLoginForm()
                # user = MyUser.objects.filter(pk=id).first()
                # if user.is_active:
                #     errormessage = '登录失败'
                # else:
                #     errormessage = '帐号未激活'
                errormessage = '登录失败,请检查帐号是否激活或者帐号密码是否正确'
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
            user = MyUser.objects.create_user(username=username, password=password, email=email, is_active=False)
            if user:
                # 注册成功
                util = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY, )
                user_id = util.dumps({'user_id': user.id}).decode('utf-8')
                mail = EmailMultiAlternatives(subject=f'点击链接激活帐号:{username}', body=f"<a href='http://127.0.0.1:8000/vote/my_active/{user_id}/'>激活</a>",from_email=settings.DEFAULT_FROM_EMAIL,to= ["594816061@qq.com", "WWW.2017.WSH.COM"])
                mail.content_subtype = 'html'
                mail.send()
                return redirect(reverse("vote:login"))

            else:
                rf = MyUserRegistForm()
                lf = MyUserLoginForm()
                errormessage = '注册失败'
                return render(req, 'test/login.html', locals())

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


def check_my_username(req):
    if req.method == "GET":
        username = req.GET.get('username')
        user = MyUser.objects.filter(username=username).first()
        if user:
            return JsonResponse({'statecode':'1'})
        else:
            return JsonResponse({'statecode':'0', 'error':'用户名不存在'})


def my_active(req, id):
    util = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY)
    obj = util.loads(id)
    id = obj['user_id']
    user = MyUser.objects.filter(pk=id).first()
    user.is_active = True
    user.save()
    return redirect(reverse('vote:login'))


def verify(request):
    if request.method == "GET":
    # 定义变量， 用于画面的背景色、 宽、 高
        bgcolor = (random.randrange(20,100),
        random.randrange(20,100),
        random.randrange(20,100))
        width = 100
        heigth = 35
        # 创建画面对象
        im = Image.new('RGB',(width,heigth),bgcolor)
        # 创建画笔对象
        draw = ImageDraw.Draw(im)
        # 调用画笔的point()函数绘制噪点
        for i in range(0, 100):
            xy = (random.randrange(0, width), random.randrange(0, heigth))
            fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
            draw.point(xy, fill=fill)
        # 定义验证码的备选值
        str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
        # 随机选取4个值作为验证码
        rand_str = ''
        for i in range(0, 4):
            rand_str += str1[random.randrange(0, len(str1))]
        # 构造字体对象
        font = ImageFont.truetype('calibrili.ttf', 23)
        fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
        # 绘制4个字
        draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
        draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
        draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
        draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
        # 释放画笔
        del draw
        request.session['verifycode'] = rand_str
        # cache.set('verifycode', rand_str, 300)
        f = io.BytesIO()
        im.save(f,'png')
        # 将内存中的图片数据返回给客户端， MIME类型为图片png
        return HttpResponse(f.getvalue(), 'image/png')
