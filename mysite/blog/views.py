from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Post

def index(request):
    return render(request, 'blog/home.html')

class PostListView(ListView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        return context

class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context
