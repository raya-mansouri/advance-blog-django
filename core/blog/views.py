from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from blog.models import Post


class IndexView(TemplateView):

    """
    a class base view to show index page
    """

    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'raya'
        context["latest_articles"] = Post.objects.all()[:5]
        return context


class PostListView(ListView):
    """ 
    get query in different ways
    
    #1
    model = Post

    #2
    def get_queryset():
        posts = Post.objects.all()
        return posts
    
    #3
    """
    queryset = Post.objects.filter(status=True)
    
    paginate_by = 5  # if pagination is desired
    context_object_name = 'posts'

    

