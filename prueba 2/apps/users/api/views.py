from rest_framework import viewsets
from django.contrib.auth import get_user_model
from apps.users.api.serializers import UserSerializer


user = get_user_model()


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer