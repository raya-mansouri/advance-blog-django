from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm


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

    #2 - we cant use order_by()
    def get_queryset():
        posts = Post.objects.all()
        return posts

    #3
    """
    queryset = Post.objects.filter(status=True)
    ordering = '-id'
    paginate_by = 3  # if pagination is desired
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm 
    success_url = reverse_lazy('blog:post-list')
    template_name_suffix = '_form'


class PostDeleteView(DeleteView):
    pass
