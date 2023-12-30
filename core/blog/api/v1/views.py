from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.generics import GenericAPIView
from .serializers import PostSerializer
from blog.models import Post


class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class PostDetail(APIView):

    # permission_classes = [IsAuthenticated]
    # serializer_class = PostSerializer

    # def get(self, request, id):
    #     post = get_object_or_404(Post, pk=id, status=True)
    #     serializer = self.serializer_class(post)
    #     return Response(serializer.data)

    # def put(self, request, id):
    #     post = get_object_or_404(Post, pk=id, status=True)
    #     serializer = PostSerializer(post, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def delete(self, request, id):
    #     post = get_object_or_404(Post, pk=id, status=True)
    #     post.delete()
    #     return Response({'detail': 'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)
