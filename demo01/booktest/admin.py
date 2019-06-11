from django.contrib import admin
from .models import BookInfo,HeroInfo

# Register your models here.


class HeroInfoInlines(admin.StackedInline):
    """关联英雄类"""
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    """模型后台管理类"""
    # 展示哪些信息
    list_display = ('title', 'pub_date')
    # 过滤器
    list_filter = ('title', 'pub_date')
    # 每页显示个数
    list_per_page = 2
    # 关联添加
    inlines = [HeroInfoInlines]


class HeroInfoAdmin(admin.ModelAdmin):
    """英雄模型后台管理类"""
    list_display = ('name', 'content')
    list_filter = ('name', 'gender')
    # 搜索框
    search_fields = ('name', 'content')


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
