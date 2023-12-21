from django.shortcuts import render
from django.views.generic.base import TemplateView

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
