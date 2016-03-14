from django.conf.urls import url, include
from blog.views import index, PostListView, PostDetailView

urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^blog/$', PostListView.as_view(), name='post-list'),
    url(r'^blog/(?P<slug>[-\w]+)$', PostDetailView.as_view(), name='post-detail'),
]
