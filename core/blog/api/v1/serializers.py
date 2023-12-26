from blog.models import Post
from rest_framework import serializers

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     author = serializers.EmailField()
#     title = serializers.CharField(max_length=200)
#     created_date = serializers.DateTimeField()

class PostSerializer(serializers.ModelSerializer):
#     
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'created_date']