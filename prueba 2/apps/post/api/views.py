from rest_framework import viewsets
from apps.post.models import Post
from apps.post.api.serializers import PostSerializer


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer