from django.contrib.syndication.views import Feed
from .models import Article


class ArticleFeed(Feed):
    title = 'wsh的个人博客'
    description = '内容广泛，跨度大'
    link = '/'

    def items(self):
        return Article.objects.all().order_by('-create_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:50]

    def item_link(self, item):
        return '/single/%s'%(item.id,)