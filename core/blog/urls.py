from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('post/',PostListView.as_view(), name='post-list'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path(
        "go-to-index/",
        RedirectView.as_view(pattern_name='blog:index'),
        name="go-to-index",
    ),
]
