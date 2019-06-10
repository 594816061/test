"""demo01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.conf.urls import url, include


# def adminpage(request):
#     """
#     处理数据
#     :param request: 代表数据请求
#     :return: 返回响应
#     """
#     return HttpResponse("这是你看到的第一个视图")


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/', adminpage),
    # 在项目路由下方添加应用路由配置文件
    url('booktest/', include('booktest.urls', namespace='booktest'))
]
