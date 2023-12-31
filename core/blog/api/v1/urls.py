from django.urls import path
from .views import *

app_name = 'api-v1'

urlpatterns = [
    path('post/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('post/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update',
         'patch': 'partial_update', 'delete': 'destroy'}), name='post-detail'),

]
