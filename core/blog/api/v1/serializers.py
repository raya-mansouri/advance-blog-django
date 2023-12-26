from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    author = serializers.EmailField()
    title = serializers.CharField(max_length=200)
    created_date = serializers.DateTimeField()