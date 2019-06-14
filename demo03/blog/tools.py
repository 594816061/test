"""
工具模块
"""
from django.core.paginator import Paginator


class GetPage:
    def get_page(self, req, art, page_time):
        paginator = Paginator(art, page_time)
        num = req.GET.get('page')
        num = 1 if num == 0 else num
        page = paginator.get_page(num)

        return page
