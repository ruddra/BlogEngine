from blog.list import PageView, ArchiveView,List1View

__author__ = 'User'
from django.conf.urls import patterns, include, url
#from django.views.generic import ListView,DetailView
from blog.models import Post
from django.contrib.syndication.views import Feed


class BlogFeed(Feed):
    title="Ruddra's Blog"
    description="My blog ruddra"
    link="/blog/feed"

    def items(self):
        return Post.objects.all().order_by('-created')[:2]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return u"/blog/%d" % item.id

urlpatterns = patterns('blog.views',
                       url(r'^$',List1View.as_view(
                           #queryset=Post.objects.all().order_by('-created')[:4],
                           #template_name='blog.html',
                       )),
                       url(r'^(?P<post_id>\d+)$', PageView.as_view(
                           model=Post,
                           #queryset=Post.objects.get()
                           #template_name="post.html",
                       )),
                       url(r'^page/(?P<page_number>\d+)$', List1View.as_view(
                           model=Post,
                           #queryset=Post.objects.get()
                           #template_name="post.html",
                       )),

                       url(r'^archives/$',ArchiveView.as_view(
                            model=Post,
                           #queryset= Post.objects.all().order_by('-created'),
                           #template_name='archives.html',
                       )),
                       url(r'^tag/(?P<tag>\w+)$', 'tagpage'),

                       url(r'^feed/$', BlogFeed()),
                       url(r'^about/$','showpage'),
                       url(r'^contact/$','contactpage'),

                       url(r'^search/$','search'),

                       )
