from rest_framework import serializers
from apps.post.models import Post
from apps.users.api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body', 'created', 'author', )
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = UserSerializer().data
        return representation
    