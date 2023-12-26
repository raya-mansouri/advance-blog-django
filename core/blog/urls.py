from django.urls import include, path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('post/',PostListView.as_view(), name='post-list'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/status/<int:pk>/', PostStatusToFalse.as_view(), name='post-status'),
    path("api/v1/", include('blog.api.v1.urls')),

    path(
        "go-to-index/",
        RedirectView.as_view(pattern_name='blog:index'),
        name="go-to-index",
    ),
]
