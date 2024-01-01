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
    # category= serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'snippet', 'category',
                  'status', 'relative_url', 'absolute_url', 'created_date', 'published_date']

    # same name as line 15    
    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self,instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)

        if request.parser_context.get('kwargs').get('pk') :
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)
        rep['category'] = CategorySerializer(instance.category).data
        return rep


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']
