from django import forms
from .models import MyUser
from django.utils.translation import gettext_lazy


# class LoginForm(forms.Form):
#     """用户表单类"""
#     # 定义表单中的邮件字段
#     email = forms.EmailField(error_messages={'required': '必须输入正确格式的邮箱'}, label='邮箱', widget=forms.EmailInput(attrs={"id": 'email'}))
#     # 用户名字段
#     username = forms.CharField(max_length=15, min_length=6, label="用户名", widget=forms.TextInput(attrs={'id': 'username'}))
#     # 密码字段
#     password = forms.CharField(max_length=15, min_length=6, widget=forms.PasswordInput(attrs={'id': 'password'}), label="密码")


class MyUserLoginForm(forms.ModelForm):
    """用户登录表单类"""
    class Meta():
        """???"""
        model = MyUser
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
        help_texts = {'username': gettext_lazy('')}


class MyUserRegistForm(forms.ModelForm):
    """用户注册表单类"""
    class Meta():
        """???"""
        model = MyUser
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
        help_texts = {'username': gettext_lazy('')}