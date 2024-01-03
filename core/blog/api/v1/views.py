from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CategorySerializer, PostSerializer
from blog.models import Post, Category
from .permissions import IsOwnerOrReadOnly

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'author', 'status']

    @action(methods=['get'], detail=False)
    def get_ok(self, request):
        return Response({'detail': 'ok'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
