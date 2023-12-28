from django.urls import path
from .views import *

app_name = 'api-v1'

urlpatterns = [
    path('post/',PostList.as_view(), name='post-list'),
    path('post/<int:id>/',post_detail, name='post-detail'),

]
