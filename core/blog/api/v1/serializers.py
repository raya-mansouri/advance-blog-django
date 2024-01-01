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
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'snippet', 'category',
                  'status', 'relative_url', 'absolute_url', 'created_date', 'published_date']

    # same name as line 15    
    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']
