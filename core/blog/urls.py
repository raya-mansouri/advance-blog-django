from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('post/',PostListView.as_view(), name='post-list'),
    path("<pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "go-to-index/",
        RedirectView.as_view(pattern_name='blog:index'),
        name="go-to-index",
    ),
]
