from blog.models import Post, Category
from rest_framework import serializers

# class PostSerializer(serializers.Serializer):
# id = serializers.IntegerField()
# author = serializers.EmailField()
# title = serializers.CharField(max_length=200)
#     created_date = serializers.DateTimeField()


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(
        source='get_absolute_api_url', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'snippet', 'category',
                  'status', 'relative_url', 'created_date', 'published_date']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']
